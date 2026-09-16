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

    # Shuffled option snapshot fields
    shuffled_option_a = db.Column(db.Text, nullable=True)
    shuffled_option_b = db.Column(db.Text, nullable=True)
    shuffled_option_c = db.Column(db.Text, nullable=True)
    shuffled_option_d = db.Column(db.Text, nullable=True)
    correct_option = db.Column(db.String(1), nullable=True)

    __table_args__ = (
        db.UniqueConstraint('exam_id', 'question_id', name='uq_exam_question'),
        db.UniqueConstraint('exam_id', 'question_order', name='uq_exam_question_order'),
    )

    def get_option_a(self):
        return self.shuffled_option_a if self.shuffled_option_a is not None else (self.question.option_a if self.question else None)

    def get_option_b(self):
        return self.shuffled_option_b if self.shuffled_option_b is not None else (self.question.option_b if self.question else None)

    def get_option_c(self):
        return self.shuffled_option_c if self.shuffled_option_c is not None else (self.question.option_c if self.question else None)

    def get_option_d(self):
        return self.shuffled_option_d if self.shuffled_option_d is not None else (self.question.option_d if self.question else None)

    def get_correct_option(self):
        return self.correct_option if self.correct_option is not None else (self.question.correct_option if self.question else None)

    def __repr__(self):
        return f"<ExamQuestion Exam:{self.exam_id} Q:{self.question_id} Order:{self.question_order}>"
