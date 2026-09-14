from flask import Blueprint

exam_bp = Blueprint('exam', __name__)

from app.exam import routes
