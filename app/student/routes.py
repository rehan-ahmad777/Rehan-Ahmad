from datetime import datetime
from flask import render_template, redirect, url_for, flash, request, session
from app.student import student_bp
from app.models import Exam, Student
from app.extensions import db

@student_bp.route('/')
def index():
    return render_template('index.html')


@student_bp.route('/exam/<token>', methods=['GET', 'POST'])
def register_exam(token):
    exam = Exam.query.filter_by(exam_token=token).first_or_404()

    if exam.is_expired():
        flash('This exam link has expired or is no longer active.', 'danger')
        return render_template('errors/exam_expired.html', exam=exam), 403

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        roll_number = request.form.get('roll_number', '').strip()
        branch = request.form.get('branch', '').strip()

        # Input validation
        if not name or not roll_number or not branch:
            flash('All fields (Name, Roll Number, Branch) are strictly compulsory.', 'danger')
            return render_template('student/register.html', exam=exam, name=name, roll_number=roll_number, branch=branch)

        # Check if student with same roll number already submitted for this exam
        existing_student = Student.query.filter_by(exam_id=exam.id, roll_number=roll_number).first()
        if existing_student and existing_student.submitted_at:
            flash(f'Roll Number {roll_number} has already completed and submitted this exam.', 'warning')
            session[f'result_access_{existing_student.id}'] = True
            return redirect(url_for('exam.student_result', student_id=existing_student.id))

        if existing_student and not existing_student.submitted_at:
            # Resume existing attempt
            student = existing_student
        else:
            # Create new exam attempt
            student = Student(
                exam_id=exam.id,
                name=name,
                roll_number=roll_number,
                branch=branch,
                started_at=datetime.utcnow()
            )
            db.session.add(student)
            db.session.commit()

        # Set active student session
        session['student_id'] = student.id
        session['exam_token'] = token

        return redirect(url_for('exam.take_exam', token=token))

    return render_template('student/register.html', exam=exam)
