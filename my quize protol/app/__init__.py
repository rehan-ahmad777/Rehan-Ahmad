import os
from flask import Flask, render_template
from config import config_by_name
from app.extensions import db, login_manager, csrf, limiter

def create_app(config_name=None):
    if config_name is None:
        debug_val = os.getenv('FLASK_DEBUG', '1')
        config_name = 'development' if debug_val in ('1', 'true', 'True') else 'production'

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_by_name.get(config_name, config_by_name['default']))

    # Ensure instance directory exists
    os.makedirs(app.instance_path, exist_ok=True)

    # If USE_SQLITE_FALLBACK is enabled or MySQL URI is default without MySQL server
    if app.config.get('USE_SQLITE_FALLBACK'):
        sqlite_file = os.path.join(app.instance_path, 'online_quiz.db')
        # Check if we should fallback to SQLite if MySQL is unavailable
        app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{sqlite_file}"

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    limiter.init_app(app)

    # Configure Login Manager
    @login_manager.user_loader
    def load_user(user_id):
        from app.models.teacher import Teacher
        return Teacher.query.get(int(user_id))

    # Register Blueprints
    from app.auth.routes import auth_bp
    from app.teacher.routes import teacher_bp
    from app.student.routes import student_bp
    from app.exam.routes import exam_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(teacher_bp, url_prefix='/teacher')
    app.register_blueprint(student_bp)
    app.register_blueprint(exam_bp)

    # Register Custom Error Handlers
    @app.errorhandler(403)
    def forbidden_error(error):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('errors/500.html'), 500

    return app
