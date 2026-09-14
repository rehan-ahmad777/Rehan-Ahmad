from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.auth import auth_bp
from app.models.teacher import Teacher
from app.extensions import limiter

@auth_bp.route('/login', methods=['GET', 'POST'])
@limiter.limit("10 per minute")
def login():
    if current_user.is_authenticated:
        return redirect(url_for('teacher.dashboard'))

    if request.method == 'POST':
        teacher_id = request.form.get('teacher_id', '').strip()
        password = request.form.get('password', '').strip()

        if not teacher_id or not password:
            flash('Both Teacher ID and Password are required.', 'danger')
            return render_template('auth/login.html')

        teacher = Teacher.query.filter_by(teacher_id=teacher_id).first()

        if teacher and teacher.check_password(password):
            login_user(teacher, remember=True)
            flash(f'Welcome back, {teacher.name}!', 'success')
            next_page = request.args.get('next')
            if next_page and next_page.startswith('/'):
                return redirect(next_page)
            return redirect(url_for('teacher.dashboard'))
        else:
            flash('Invalid Teacher ID or Password. Please try again.', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('auth.login'))
