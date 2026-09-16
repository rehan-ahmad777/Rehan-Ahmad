from datetime import datetime
from flask import render_template, redirect, url_for, flash, request, session, jsonify, abort
from flask_login import current_user
from app.exam import exam_bp
from app.models import Exam, ExamQuestion, Question, Student, StudentAnswer, Result
from app.extensions import db

def process_and_finalize_submission(student, exam):
    """
    Server-side evaluation logic. Calculates score, saves answers, creates result record,
    and locks the exam attempt.
    """
    if student.submitted_at or Result.query.filter_by(student_id=student.id).first():
        return Result.query.filter_by(student_id=student.id).first()

    # Get exam questions ordered
    eq_list = ExamQuestion.query.filter_by(exam_id=exam.id).order_by(ExamQuestion.question_order).all()
    
    # Get answers recorded in DB
    existing_answers = {sa.question_id: sa for sa in StudentAnswer.query.filter_by(student_id=student.id).all()}

    correct_count = 0
    wrong_count = 0
    unanswered_count = 0

    for eq in eq_list:
        question = Question.query.get(eq.question_id)
        ans_record = existing_answers.get(question.id)
        
        selected = ans_record.selected_option if ans_record else None
        
        if not selected or selected not in ['A', 'B', 'C', 'D']:
            unanswered_count += 1
            is_correct = False
        elif selected == question.correct_option:
            correct_count += 1
            is_correct = True
        else:
            wrong_count += 1
            is_correct = False

        if ans_record:
            ans_record.is_correct = is_correct
        else:
            new_ans = StudentAnswer(
                student_id=student.id,
                question_id=question.id,
                selected_option=selected,
                is_correct=is_correct
            )
            db.session.add(new_ans)

    total_q = len(eq_list)
    marks_obtained = correct_count * 1 # 1 question = 1 mark
    percentage = round((marks_obtained / total_q) * 100, 2) if total_q > 0 else 0.0

    student.submitted_at = datetime.utcnow()

    result = Result(
        student_id=student.id,
        exam_id=exam.id,
        total_questions=total_q,
        correct_answers=correct_count,
        wrong_answers=wrong_count,
        unanswered=unanswered_count,
        marks_obtained=marks_obtained,
        percentage=percentage,
        submitted_at=student.submitted_at
    )

    db.session.add(result)
    db.session.commit()
    
    return result


@exam_bp.route('/exam/<token>/take')
@exam_bp.route('/exam/<token>/start')
def take_exam(token):
    exam = Exam.query.filter((Exam.exam_code == token) | (Exam.exam_token == token)).first_or_404()
    student_id = session.get('student_id')

    if not student_id:
        flash('Please register your student details before starting the exam.', 'warning')
        return redirect(url_for('student.register_exam', exam_code=exam.exam_code))

    student = Student.query.get_or_404(student_id)
    
    if student.exam_id != exam.id:
        flash('Invalid session token for this exam.', 'danger')
        return redirect(url_for('student.register_exam', exam_code=exam.exam_code))

    # Check if already submitted
    if student.submitted_at or Result.query.filter_by(student_id=student.id).first():
        session[f'result_access_{student.id}'] = True
        flash('You have already submitted this exam.', 'info')
        return redirect(url_for('exam.student_result', student_id=student.id))

    # Calculate remaining time in seconds (Backend enforcement)
    elapsed_seconds = (datetime.utcnow() - student.started_at).total_seconds()
    allowed_seconds = exam.duration * 60
    remaining_seconds = max(0, int(allowed_seconds - elapsed_seconds))

    # If backend timer expired, automatically finalize and submit
    if remaining_seconds <= 0:
        result = process_and_finalize_submission(student, exam)
        session[f'result_access_{student.id}'] = True
        flash('Time expired! Your exam has been automatically submitted.', 'warning')
        return redirect(url_for('exam.student_result', student_id=student.id))

    # Fetch fixed exam questions in specified order
    eq_records = ExamQuestion.query.filter_by(exam_id=exam.id).order_by(ExamQuestion.question_order).all()
    questions_data = []
    
    # Existing answers map
    existing_answers = {sa.question_id: sa.selected_option for sa in StudentAnswer.query.filter_by(student_id=student.id).all()}

    for eq in eq_records:
        q = Question.query.get(eq.question_id)
        questions_data.append({
            'order': eq.question_order,
            'id': q.id,
            'text': q.question_text,
            'option_a': q.option_a,
            'option_b': q.option_b,
            'option_c': q.option_c,
            'option_d': q.option_d,
            'selected': existing_answers.get(q.id)
        })

    return render_template(
        'student/take_exam.html',
        exam=exam,
        student=student,
        questions=questions_data,
        remaining_seconds=remaining_seconds
    )


@exam_bp.route('/exam/<token>/save-answer', methods=['POST'])
def save_answer(token):
    exam = Exam.query.filter((Exam.exam_code == token) | (Exam.exam_token == token)).first_or_404()
    student_id = session.get('student_id')

    if not student_id:
        return jsonify({'status': 'error', 'message': 'Unauthorized session'}), 401

    student = Student.query.get(student_id)
    if not student or student.submitted_at:
        return jsonify({'status': 'error', 'message': 'Attempt locked'}), 403

    data = request.get_json() or {}
    question_id = data.get('question_id')
    selected_option = data.get('selected_option')

    if selected_option and selected_option not in ['A', 'B', 'C', 'D']:
        selected_option = None

    if question_id:
        ans_record = StudentAnswer.query.filter_by(student_id=student.id, question_id=question_id).first()
        if ans_record:
            ans_record.selected_option = selected_option
        else:
            ans_record = StudentAnswer(
                student_id=student.id,
                question_id=question_id,
                selected_option=selected_option
            )
            db.session.add(ans_record)
        
        db.session.commit()

    return jsonify({'status': 'success'})


@exam_bp.route('/exam/<token>/submit', methods=['POST'])
def submit_exam(token):
    exam = Exam.query.filter((Exam.exam_code == token) | (Exam.exam_token == token)).first_or_404()
    student_id = session.get('student_id')

    if not student_id:
        flash('Session expired. Could not complete submission.', 'danger')
        return redirect(url_for('student.register_exam', exam_code=exam.exam_code))

    student = Student.query.get_or_404(student_id)

    # Collect answers submitted in final POST form if any
    for key, value in request.form.items():
        if key.startswith('q_'):
            try:
                q_id = int(key.split('_')[1])
                opt = value.strip().upper() if value else None
                if opt in ['A', 'B', 'C', 'D']:
                    ans_record = StudentAnswer.query.filter_by(student_id=student.id, question_id=q_id).first()
                    if ans_record:
                        ans_record.selected_option = opt
                    else:
                        ans_record = StudentAnswer(
                            student_id=student.id,
                            question_id=q_id,
                            selected_option=opt
                        )
                        db.session.add(ans_record)
            except ValueError:
                continue

    db.session.commit()

    result = process_and_finalize_submission(student, exam)
    session[f'result_access_{student.id}'] = True
    flash('Exam submitted successfully!', 'success')
    return redirect(url_for('exam.student_result', student_id=student.id))


@exam_bp.route('/exam/result/<int:student_id>')
@exam_bp.route('/exam/<exam_code>/result/<int:student_id>')
def student_result(student_id, exam_code=None):
    student = Student.query.get_or_404(student_id)
    result = Result.query.filter_by(student_id=student.id).first_or_404()
    exam = Exam.query.get(student.exam_id)

    # Security check:
    # 1. Is teacher who created the exam logged in?
    # 2. OR is current student session token matching this student?
    is_teacher_owner = current_user.is_authenticated and exam.teacher_id == current_user.id
    is_student_session = session.get('student_id') == student.id or session.get(f'result_access_{student.id}') is True

    if not (is_teacher_owner or is_student_session):
        abort(403)

    # Detailed Question Review
    eq_records = ExamQuestion.query.filter_by(exam_id=exam.id).order_by(ExamQuestion.question_order).all()
    student_answers = {sa.question_id: sa for sa in StudentAnswer.query.filter_by(student_id=student.id).all()}

    question_reviews = []
    for eq in eq_records:
        q = Question.query.get(eq.question_id)
        sa = student_answers.get(q.id)
        user_choice = sa.selected_option if sa else None
        
        if not user_choice:
            status = 'Unanswered'
            status_class = 'bg-secondary'
        elif user_choice == q.correct_option:
            status = 'Correct'
            status_class = 'bg-success'
        else:
            status = 'Wrong'
            status_class = 'bg-danger'

        question_reviews.append({
            'order': eq.question_order,
            'text': q.question_text,
            'option_a': q.option_a,
            'option_b': q.option_b,
            'option_c': q.option_c,
            'option_d': q.option_d,
            'user_choice': user_choice,
            'correct_option': q.correct_option,
            'status': status,
            'status_class': status_class
        })

    return render_template(
        'student/result.html',
        student=student,
        result=result,
        exam=exam,
        reviews=question_reviews
    )
