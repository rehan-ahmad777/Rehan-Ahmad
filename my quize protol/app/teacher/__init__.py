from flask import Blueprint

teacher_bp = Blueprint('teacher', __name__)

from app.teacher import routes
