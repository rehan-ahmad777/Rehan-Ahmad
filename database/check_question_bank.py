import os
import sys
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.question_data.grammar import GRAMMAR_QUESTIONS
from database.question_data.physics import PHYSICS_QUESTIONS
from database.question_data.chemistry import CHEMISTRY_QUESTIONS
from database.question_data.maths import MATHS_QUESTIONS
from app.question_validator import normalize_question_text

def analyze_dataset(subject_name, questions):
    total = len(questions)
    exact_map = {}
    near_map = {}

    for idx, q in enumerate(questions, start=1):
        q_text = q.get('question_text', '').strip()
        
        # Exact duplicate check
        if q_text in exact_map:
            exact_map[q_text].append(idx)
        else:
            exact_map[q_text] = [idx]

        # Near duplicate check (normalized)
        norm = normalize_question_text(q_text)
        if norm in near_map:
            near_map[norm].append((idx, q_text))
        else:
            near_map[norm] = [(idx, q_text)]

    exact_duplicates = {k: v for k, v in exact_map.items() if len(v) > 1}
    near_duplicates = {k: v for k, v in near_map.items() if len(v) > 1}

    unique_count = len(near_map)
    duplicate_count = total - unique_count

    print(f"\n{subject_name}:")
    print(f"{total} total")
    print(f"{unique_count} unique")
    print(f"{duplicate_count} duplicates")

    if near_duplicates:
        print("--- DUPLICATE / NEAR-DUPLICATE DETECTED ---")
        for norm, occurrences in near_duplicates.items():
            indices = [occ[0] for occ in occurrences]
            print(f"Indices {indices}: '{occurrences[0][1]}'")
    
    return total, unique_count, duplicate_count

def simulate_exam_generations():
    from app import create_app
    from app.models import Subject, Question, Exam, ExamQuestion, Teacher
    import random

    app = create_app('testing')
    with app.app_context():
        from app.extensions import db
        db.create_all()
        from database.seed_questions import seed_database
        seed_database(app=app, force_reseed=True)

        teacher = Teacher.query.first()
        sub = Subject.query.filter_by(name='Grammar').first()

        print("==================================================")
        print(" SIMULATING 3 RANDOM EXAM GENERATIONS (Grammar)")
        print("==================================================")

        for exam_num in range(1, 4):
            available = Question.query.filter_by(subject_id=sub.id).all()
            selected = random.sample(available, 5) # Pick 5 sample questions
            random.shuffle(selected)
            q_ids = [q.id for q in selected]

            print(f"\nExam {exam_num} Selected Question IDs: {q_ids}")
            for idx, q in enumerate(selected, start=1):
                print(f"  Question {idx} [DB ID {q.id}]: {q.question_text[:60]}...")

            assert len(q_ids) == len(set(q_ids)), "Exam must not contain duplicate question IDs!"

def run_full_check():
    datasets = {
        'Grammar': GRAMMAR_QUESTIONS,
        'Physics': PHYSICS_QUESTIONS,
        'Chemistry': CHEMISTRY_QUESTIONS,
        'Maths': MATHS_QUESTIONS
    }

    print("==================================================")
    print(" QUESTION BANK DUPLICATE & INTEGRITY REPORT")
    print("==================================================")

    all_clean = True
    for sub, q_list in datasets.items():
        total, unique, dupes = analyze_dataset(sub, q_list)
        if dupes > 0 or total != 100:
            all_clean = False

    print("\n==================================================")
    if all_clean:
        print(" RESULT: ALL 400 QUESTIONS ARE 100% UNIQUE & VALID!")
    else:
        print(" RESULT: DUPLICATES OR COUNT MISMATCHES FOUND!")
    print("==================================================\n")

    simulate_exam_generations()

if __name__ == '__main__':
    run_full_check()
