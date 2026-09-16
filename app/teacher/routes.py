import random
import string
from datetime import datetime, timedelta
from flask import render_template, redirect, url_for, flash, request, abort, jsonify, current_app
from flask_login import login_required, current_user
from app.teacher import teacher_bp
from app.models import Subject, Question, Exam, ExamQuestion, Student, Result
from app.extensions import db

def generate_exam_code():
    chars = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(random.choices(chars, k=6))
        if not Exam.query.filter_by(exam_code=code).first():
            return code

@teacher_bp.route('/login')
def teacher_login():
    return redirect(url_for('auth.login'))

@teacher_bp.route('/logout')
@login_required
def teacher_logout():
    return redirect(url_for('auth.logout'))

@teacher_bp.route('/dashboard')
@login_required
def dashboard():
    subjects = Subject.query.all()
    subject_cards = []
    
    for sub in subjects:
        q_count = Question.query.filter_by(subject_id=sub.id).count()
        subject_cards.append({
            'id': sub.id,
            'name': sub.name,
            'question_count': q_count
        })

    # Recent exams created by this teacher
    teacher_exams = Exam.query.filter_by(teacher_id=current_user.id).order_by(Exam.created_at.desc()).all()
    
    return render_template(
        'teacher/dashboard.html', 
        subject_cards=subject_cards, 
        exams=teacher_exams,
        total_exams=len(teacher_exams)
    )

@teacher_bp.route('/exams')
@login_required
def my_exams():
    return redirect(url_for('teacher.dashboard'))

@teacher_bp.route('/exam/create', methods=['GET', 'POST'])
@login_required
def exam_create_default():
    # If no subject selected, default to first subject or render dashboard
    first_subject = Subject.query.first()
    if first_subject:
        return redirect(url_for('teacher.create_exam', subject_id=first_subject.id))
    flash('No subjects found in database.', 'danger')
    return redirect(url_for('teacher.dashboard'))

@teacher_bp.route('/create-exam/<int:subject_id>', methods=['GET', 'POST'])
@login_required
def create_exam(subject_id):
    subject = Subject.query.get_or_404(subject_id)
    available_questions = Question.query.filter_by(subject_id=subject.id).all()
    available_count = len(available_questions)

    if available_count == 0:
        flash(f'Cannot create exam for {subject.name}. No questions available in question bank.', 'danger')
        return redirect(url_for('teacher.dashboard'))

    if request.method == 'POST':
        try:
            total_q = int(request.form.get('total_questions', 0))
            duration = int(request.form.get('duration', 0))
        except ValueError:
            flash('Total questions and duration must be valid positive numbers.', 'danger')
            return render_template('teacher/create_exam.html', subject=subject, available_count=available_count)

        # Validation rules
        if total_q <= 0:
            flash('Total marks/questions must be at least 1.', 'danger')
            return render_template('teacher/create_exam.html', subject=subject, available_count=available_count)

        if total_q > available_count:
            flash(f'Only {available_count} questions are available for {subject.name}. Please enter a smaller number.', 'danger')
            return render_template('teacher/create_exam.html', subject=subject, available_count=available_count)

        if duration <= 0 or duration > 300:
            flash('Exam duration must be between 1 and 300 minutes.', 'danger')
            return render_template('teacher/create_exam.html', subject=subject, available_count=available_count)

        # 1 question = 1 mark
        total_marks = total_q
        
        # Server-side random question selection (Secure & Non-duplicate)
        selected_questions = random.sample(available_questions, total_q)
        random.shuffle(selected_questions) # Shuffle question display order
        
        exam_code = generate_exam_code()
        exam_token = Exam.generate_token()
        
        # Expiry time (default active duration + extra operational window)
        expires_at = datetime.utcnow() + timedelta(days=7)

        exam = Exam(
            subject_id=subject.id,
            teacher_id=current_user.id,
            exam_code=exam_code,
            exam_token=exam_token,
            total_questions=total_q,
            total_marks=total_marks,
            duration=duration,
            expires_at=expires_at,
            status='active'
        )
        db.session.add(exam)
        db.session.flush()

        # Fix exam questions order & snapshot shuffled options
        for order, q in enumerate(selected_questions, start=1):
            # Option Shuffling with dynamic correct_option remapping
            orig_opts = {
                'A': q.option_a,
                'B': q.option_b,
                'C': q.option_c,
                'D': q.option_d
            }
            correct_text = orig_opts.get(q.correct_option, q.option_a)
            
            option_list = [q.option_a, q.option_b, q.option_c, q.option_d]
            random.shuffle(option_list)

            shuffled_a, shuffled_b, shuffled_c, shuffled_d = option_list

            if shuffled_a == correct_text:
                remapped_correct = 'A'
            elif shuffled_b == correct_text:
                remapped_correct = 'B'
            elif shuffled_c == correct_text:
                remapped_correct = 'C'
            else:
                remapped_correct = 'D'

            eq = ExamQuestion(
                exam_id=exam.id,
                question_id=q.id,
                question_order=order,
                shuffled_option_a=shuffled_a,
                shuffled_option_b=shuffled_b,
                shuffled_option_c=shuffled_c,
                shuffled_option_d=shuffled_d,
                correct_option=remapped_correct
            )
            db.session.add(eq)

        db.session.commit()
        flash('Exam created successfully! Share the generated link with your students.', 'success')
        return redirect(url_for('teacher.exam_created', token=exam.exam_token))

    return render_template('teacher/create_exam.html', subject=subject, available_count=available_count)


def get_public_exam_url(exam_code):
    """
    Constructs the official public shareable student URL for the given exam_code.
    Uses request context dynamically when available so local testing generates local URLs
    and production generates Render URLs.
    """
    if request:
        scheme = request.headers.get('X-Forwarded-Proto', request.scheme)
        host = request.host
        return f"{scheme}://{host}/exam/{exam_code}"
    
    base_url = current_app.config.get('PUBLIC_URL', 'https://rehan-ahmad-1.onrender.com').rstrip('/')
    return f"{base_url}/exam/{exam_code}"

@teacher_bp.route('/exam/<token>/created')
@login_required
def exam_created(token):
    exam = Exam.query.filter((Exam.exam_token == token) | (Exam.exam_code == token)).first_or_404()
    
    # Strict Authorization check
    if exam.teacher_id != current_user.id:
        abort(403)

    exam_url = get_public_exam_url(exam.exam_code)

    return render_template(
        'teacher/exam_created.html', 
        exam=exam, 
        exam_url=exam_url
    )

@teacher_bp.route('/exam/<int:exam_id>/share')
@login_required
def share_exam_by_id(exam_id):
    exam = Exam.query.get_or_404(exam_id)
    if exam.teacher_id != current_user.id:
        abort(403)
    return redirect(url_for('teacher.exam_created', token=exam.exam_token))

@teacher_bp.route('/exam/<int:exam_id>/disable', methods=['GET', 'POST'])
@login_required
def disable_exam(exam_id):
    exam = Exam.query.get_or_404(exam_id)
    if exam.teacher_id != current_user.id:
        abort(403)

    if exam.status == 'active':
        exam.status = 'disabled'
        flash(f'Exam {exam.exam_code} has been disabled. Students can no longer access it.', 'warning')
    else:
        exam.status = 'active'
        flash(f'Exam {exam.exam_code} has been re-activated.', 'success')

    db.session.commit()
    return redirect(url_for('teacher.dashboard'))

@teacher_bp.route('/exam/<int:exam_id>/results')
@login_required
def exam_results_by_id(exam_id):
    return redirect(url_for('teacher.results', exam_id=exam_id))


@teacher_bp.route('/results')
@login_required
def results():
    # Only fetch exams created by this teacher
    exams = Exam.query.filter_by(teacher_id=current_user.id).order_by(Exam.created_at.desc()).all()
    exam_ids = [e.id for e in exams]

    if not exam_ids:
        return render_template('teacher/results.html', exams=[], results=[], stats={})

    selected_exam_id = request.args.get('exam_id', type=int)
    search_query = request.args.get('q', '').strip()
    branch_filter = request.args.get('branch', '').strip()
    sort_by = request.args.get('sort', 'date_desc')

    # Query results joined with Student and Exam
    query = db.session.query(Result, Student, Exam).\
        join(Student, Result.student_id == Student.id).\
        join(Exam, Result.exam_id == Exam.id).\
        filter(Exam.teacher_id == current_user.id)

    if selected_exam_id:
        query = query.filter(Result.exam_id == selected_exam_id)

    if search_query:
        search_pattern = f"%{search_query}%"
        query = query.filter(
            (Student.name.like(search_pattern)) | 
            (Student.roll_number.like(search_pattern)) |
            (Exam.exam_code.like(search_pattern))
        )

    if branch_filter:
        query = query.filter(Student.branch == branch_filter)

    # Sorting
    if sort_by == 'marks_desc':
        query = query.order_by(Result.marks_obtained.desc())
    elif sort_by == 'marks_asc':
        query = query.order_by(Result.marks_obtained.asc())
    elif sort_by == 'pct_desc':
        query = query.order_by(Result.percentage.desc())
    elif sort_by == 'pct_asc':
        query = query.order_by(Result.percentage.asc())
    else:
        query = query.order_by(Result.submitted_at.desc())

    all_results = query.all()

    # Get distinct branches for filter dropdown
    branches = db.session.query(Student.branch).join(Exam).filter(Exam.teacher_id == current_user.id).distinct().all()
    branches_list = [b[0] for b in branches if b[0]]

    # Statistics calculation
    total_students = len(all_results)
    if total_students > 0:
        percentages = [r.Result.percentage for r in all_results]
        marks = [r.Result.marks_obtained for r in all_results]
        highest_score = max(marks)
        average_score = round(sum(marks) / total_students, 2)
        pass_count = sum(1 for p in percentages if p >= 40.0)
        fail_count = total_students - pass_count
    else:
        highest_score = 0
        average_score = 0
        pass_count = 0
        fail_count = 0

    stats = {
        'total_students': total_students,
        'highest_score': highest_score,
        'average_score': average_score,
        'pass_count': pass_count,
        'fail_count': fail_count,
        'pass_percentage': round((pass_count / total_students * 100), 1) if total_students > 0 else 0
    }

    return render_template(
        'teacher/results.html',
        exams=exams,
        selected_exam_id=selected_exam_id,
        results=all_results,
        branches=branches_list,
        stats=stats,
        search_query=search_query,
        branch_filter=branch_filter,
        sort_by=sort_by
    )
