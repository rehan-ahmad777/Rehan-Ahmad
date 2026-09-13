from datetime import datetime
from app.extensions import db

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id', ondelete='CASCADE'), nullable=False, index=True)
    name = db.Column(db.String(100), nullable=False)
    roll_number = db.Column(db.String(50), nullable=False)
    branch = db.Column(db.String(100), nullable=False)
    started_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    submitted_at = db.Column(db.DateTime, nullable=True)

    # Relationships
    answers = db.relationship('StudentAnswer', backref='student', lazy='dynamic', cascade='all, delete-orphan')
    result = db.relationship('Result', backref='student', uselist=False, cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Student {self.name} - Roll {self.roll_number}>"


class StudentAnswer(db.Model):
    __tablename__ = 'student_answers'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id', ondelete='CASCADE'), nullable=False, index=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id', ondelete='CASCADE'), nullable=False, index=True)
    selected_option = db.Column(db.String(1), nullable=True) # 'A', 'B', 'C', 'D' or None
    is_correct = db.Column(db.Boolean, default=False, nullable=False)

    __table_args__ = (
        db.UniqueConstraint('student_id', 'question_id', name='uq_student_question_answer'),
    )

    def __repr__(self):
        return f"<StudentAnswer Student:{self.student_id} Q:{self.question_id} Choice:{self.selected_option}>"


class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id', ondelete='CASCADE'), unique=True, nullable=False, index=True)
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id', ondelete='CASCADE'), nullable=False, index=True)
    total_questions = db.Column(db.Integer, nullable=False)
    correct_answers = db.Column(db.Integer, nullable=False)
    wrong_answers = db.Column(db.Integer, nullable=False)
    unanswered = db.Column(db.Integer, nullable=False)
    marks_obtained = db.Column(db.Integer, nullable=False)
    percentage = db.Column(db.Float, nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<Result Student:{self.student_id} Score:{self.marks_obtained}/{self.total_questions}>"
