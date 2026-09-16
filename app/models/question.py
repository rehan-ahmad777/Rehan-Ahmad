from datetime import datetime
from app.extensions import db

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id', ondelete='CASCADE'), nullable=False, index=True)
    question_text = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.Text, nullable=False)
    option_b = db.Column(db.Text, nullable=False)
    option_c = db.Column(db.Text, nullable=False)
    option_d = db.Column(db.Text, nullable=False)
    correct_option = db.Column(db.String(1), nullable=False) # 'A', 'B', 'C', 'D'
    explanation = db.Column(db.Text, nullable=True)
    difficulty = db.Column(db.String(20), default='High', nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    exam_questions = db.relationship('ExamQuestion', backref='question', lazy='dynamic', cascade='all, delete-orphan')

    def to_dict(self, include_correct=False):
        data = {
            'id': self.id,
            'question_text': self.question_text,
            'option_a': self.option_a,
            'option_b': self.option_b,
            'option_c': self.option_c,
            'option_d': self.option_d,
            'explanation': self.explanation,
            'difficulty': self.difficulty
        }
        if include_correct:
            data['correct_option'] = self.correct_option
        return data

    def __repr__(self):
        return f"<Question {self.id} - Subject {self.subject_id}>"
