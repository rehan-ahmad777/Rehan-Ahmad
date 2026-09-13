import uuid
from datetime import datetime, timedelta
from app.extensions import db

class Exam(db.Model):
    __tablename__ = 'exams'

    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id', ondelete='CASCADE'), nullable=False, index=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id', ondelete='CASCADE'), nullable=False, index=True)
    exam_code = db.Column(db.String(20), unique=True, nullable=False, index=True)
    exam_token = db.Column(db.String(64), unique=True, nullable=False, index=True)
    total_questions = db.Column(db.Integer, nullable=False)
    total_marks = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False) # Duration in minutes
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(20), default='active', nullable=False) # 'active', 'closed'

    # Relationships
    exam_questions = db.relationship(
        'ExamQuestion', 
        backref='exam', 
        lazy='joined', 
        order_by='ExamQuestion.question_order',
        cascade='all, delete-orphan'
    )
    students = db.relationship('Student', backref='exam', lazy='dynamic', cascade='all, delete-orphan')
    results = db.relationship('Result', backref='exam', lazy='dynamic', cascade='all, delete-orphan')

    @staticmethod
    def generate_token():
        return uuid.uuid4().hex

    def is_expired(self):
        if self.status != 'active':
            return True
        if self.expires_at and datetime.utcnow() > self.expires_at:
            return True
        return False

    def __repr__(self):
        return f"<Exam {self.exam_code} - Token {self.exam_token[:8]}>"


class ExamQuestion(db.Model):
    __tablename__ = 'exam_questions'

    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id', ondelete='CASCADE'), nullable=False, index=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id', ondelete='CASCADE'), nullable=False, index=True)
    question_order = db.Column(db.Integer, nullable=False)

    __table_args__ = (
        db.UniqueConstraint('exam_id', 'question_id', name='uq_exam_question'),
        db.UniqueConstraint('exam_id', 'question_order', name='uq_exam_question_order'),
    )

    def __repr__(self):
        return f"<ExamQuestion Exam:{self.exam_id} Q:{self.question_id} Order:{self.question_order}>"
