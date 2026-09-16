import os
import sys

# Ensure root dir is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.extensions import db
from app.models import Teacher, Subject, Question
from app.question_validator import validate_question_data, normalize_question_text
from database.question_data.grammar import GRAMMAR_QUESTIONS
from database.question_data.physics import PHYSICS_QUESTIONS
from database.question_data.chemistry import CHEMISTRY_QUESTIONS
from database.question_data.maths import MATHS_QUESTIONS

def seed_database(app=None, force_reseed=False):
    if app is None:
        from flask import current_app
        if current_app:
            app = current_app._get_current_object()
        else:
            app = create_app(os.getenv('FLASK_ENV', 'development'))

    with app.app_context():
        print("Initializing database tables...")
        db.create_all()

        # 1. Seed Default Teacher
        teacher = Teacher.query.filter_by(teacher_id='T1001').first()
        if not teacher:
            teacher = Teacher(
                teacher_id='T1001',
                name='Dr. Alan Turing'
            )
            teacher.set_password('Teacher@123')
            db.session.add(teacher)
            print("Created default teacher: ID 'T1001', Password 'Teacher@123'")
        else:
            print("Default teacher 'T1001' already exists.")

        # 2. Seed Subjects
        subject_names = ['Grammar', 'Physics', 'Chemistry', 'Maths']
        subject_map = {}
        for name in subject_names:
            sub = Subject.query.filter_by(name=name).first()
            if not sub:
                sub = Subject(name=name)
                db.session.add(sub)
                db.session.flush()
                print(f"Created subject: {name}")
            subject_map[name] = sub

        # Ensure 'Mathematics' alias points to 'Maths' if present
        math_alias = Subject.query.filter_by(name='Mathematics').first()
        if math_alias:
            subject_map['Mathematics'] = math_alias
        else:
            subject_map['Mathematics'] = subject_map['Maths']

        db.session.commit()

        # 3. Datasets mapping
        datasets = {
            'Grammar': GRAMMAR_QUESTIONS,
            'Physics': PHYSICS_QUESTIONS,
            'Chemistry': CHEMISTRY_QUESTIONS,
            'Maths': MATHS_QUESTIONS
        }

        total_inserted = 0
        total_validated = 0

        for sub_name, q_list in datasets.items():
            subject = subject_map[sub_name]
            existing_count = Question.query.filter_by(subject_id=subject.id).count()

            if existing_count < 100 or force_reseed:
                print(f"Seeding high-quality question bank for {sub_name} (Existing: {existing_count})...")
                
                # Delete existing questions for subject if reseeding
                if existing_count > 0:
                    Question.query.filter_by(subject_id=subject.id).delete()
                    db.session.flush()

                existing_normalized = set()
                sub_inserted = 0

                for q_dict in q_list:
                    # Inject subject for validator
                    q_dict_copy = dict(q_dict)
                    q_dict_copy['subject'] = sub_name

                    is_valid, err_msg = validate_question_data(q_dict_copy, existing_normalized)
                    if not is_valid:
                        raise ValueError(f"Validation failed for question in {sub_name}: {err_msg}\nQuestion: {q_dict_copy.get('question_text')}")

                    norm_text = normalize_question_text(q_dict_copy['question_text'])
                    existing_normalized.add(norm_text)

                    q_obj = Question(
                        subject_id=subject.id,
                        question_text=q_dict_copy['question_text'].strip(),
                        option_a=q_dict_copy['option_a'].strip(),
                        option_b=q_dict_copy['option_b'].strip(),
                        option_c=q_dict_copy['option_c'].strip(),
                        option_d=q_dict_copy['option_d'].strip(),
                        correct_option=q_dict_copy['correct_option'].strip().upper(),
                        explanation=q_dict_copy.get('explanation', '').strip(),
                        difficulty=q_dict_copy.get('difficulty', 'High').strip()
                    )
                    db.session.add(q_obj)
                    sub_inserted += 1
                    total_validated += 1

                db.session.commit()
                total_inserted += sub_inserted
                print(f"Successfully validated & seeded exactly {sub_inserted} high-quality questions for {sub_name}.")
            else:
                print(f"Subject '{sub_name}' already contains {existing_count} validated questions.")

        print(f"Database seed process completed cleanly! Total questions processed: {total_validated}")

if __name__ == '__main__':
    seed_database(force_reseed=True)
