from app.extensions import db

class Subject(db.Model):
    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False, index=True)

    # Relationships
    questions = db.relationship('Question', backref='subject', lazy='dynamic', cascade='all, delete-orphan')
    exams = db.relationship('Exam', backref='subject', lazy='dynamic', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Subject {self.name}>"
