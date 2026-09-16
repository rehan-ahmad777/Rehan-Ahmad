from datetime import datetime
from flask import render_template, redirect, url_for, flash, request, session
from app.student import student_bp
from app.models import Exam, Student
from app.extensions import db

from sqlalchemy import func

@student_bp.route('/')
def index():
    return render_template('index.html')


@student_bp.route('/exam/<exam_code>', methods=['GET', 'POST'])
def register_exam(exam_code):
    clean_code = (exam_code or '').strip()
    exam = Exam.query.filter(
        (func.lower(Exam.exam_code) == clean_code.lower()) |
        (Exam.exam_code == clean_code) |
        (Exam.exam_token == clean_code)
    ).first()

    if not exam:
        return render_template('errors/404.html'), 404

    if exam.status != 'active' or exam.is_expired():
        flash('This exam is no longer available.', 'danger')
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
        session['exam_token'] = exam.exam_token
        session['exam_code'] = exam.exam_code

        return redirect(url_for('exam.take_exam', token=exam.exam_code))

    return render_template('student/register.html', exam=exam)
