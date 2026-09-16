import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.extensions import db
from app.models import Teacher, Subject, Question, Exam, ExamQuestion, Student, StudentAnswer, Result
from app.question_validator import validate_question_data, normalize_question_text
from database.seed_questions import seed_database

class QuestionBankAndExamTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        db.drop_all()
        db.create_all()
        seed_database(app=self.app, force_reseed=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def login_teacher(self):
        return self.client.post('/auth/login', data={
            'teacher_id': 'T1001',
            'password': 'Teacher@123'
        }, follow_redirects=True)

    # 1. Total 400 questions check
    def test_total_question_count(self):
        total = Question.query.count()
        self.assertEqual(total, 400, f"Expected exactly 400 questions, found {total}")

    # 2 - 5. Subject-wise 100 count check
    def test_subject_wise_counts(self):
        subjects = ['Grammar', 'Physics', 'Chemistry', 'Maths']
        for sub_name in subjects:
            sub = Subject.query.filter_by(name=sub_name).first()
            self.assertIsNotNone(sub, f"Subject {sub_name} should exist")
            count = Question.query.filter_by(subject_id=sub.id).count()
            self.assertEqual(count, 100, f"Subject {sub_name} must have exactly 100 questions, found {count}")

    # 6. No duplicate normalized question text
    def test_no_duplicate_questions(self):
        questions = Question.query.all()
        seen = set()
        duplicates = []
        for q in questions:
            norm = normalize_question_text(q.question_text)
            if norm in seen:
                duplicates.append(q.question_text)
            seen.add(norm)
        self.assertEqual(len(duplicates), 0, f"Found duplicate questions: {duplicates}")

    # 7. Every question has 4 non-empty options
    def test_all_questions_have_4_options(self):
        questions = Question.query.all()
        for q in questions:
            self.assertTrue(bool(q.option_a and q.option_a.strip()), f"Q{q.id} missing option_a")
            self.assertTrue(bool(q.option_b and q.option_b.strip()), f"Q{q.id} missing option_b")
            self.assertTrue(bool(q.option_c and q.option_c.strip()), f"Q{q.id} missing option_c")
            self.assertTrue(bool(q.option_d and q.option_d.strip()), f"Q{q.id} missing option_d")

    # 8. Every correct_option is A/B/C/D and non-empty explanation
    def test_valid_correct_option_and_explanation(self):
        questions = Question.query.all()
        for q in questions:
            self.assertIn(q.correct_option, ['A', 'B', 'C', 'D'], f"Q{q.id} invalid correct_option '{q.correct_option}'")
            self.assertTrue(bool(q.explanation and q.explanation.strip()), f"Q{q.id} missing explanation")

    # 9 & 10. Exam contains requested question count without internal duplicates
    def test_exam_random_selection_no_duplicates(self):
        self.login_teacher()
        sub = Subject.query.filter_by(name='Grammar').first()
        res = self.client.post(f'/teacher/create-exam/{sub.id}', data={
            'total_questions': 20,
            'duration': 30
        }, follow_redirects=True)
        self.assertEqual(res.status_code, 200)

        exam = Exam.query.filter_by(subject_id=sub.id).first()
        self.assertIsNotNone(exam)
        eqs = ExamQuestion.query.filter_by(exam_id=exam.id).all()
        self.assertEqual(len(eqs), 20)

        q_ids = [eq.question_id for eq in eqs]
        self.assertEqual(len(q_ids), len(set(q_ids)), "Exam must not contain duplicate questions")

    # 11 & 12 & 13. Question & Option Shuffling + Correct Answer Remapping
    def test_option_shuffling_and_correct_remapping(self):
        self.login_teacher()
        sub = Subject.query.filter_by(name='Physics').first()
        self.client.post(f'/teacher/create-exam/{sub.id}', data={
            'total_questions': 10,
            'duration': 15
        })

        exam = Exam.query.filter_by(subject_id=sub.id).first()
        eqs = ExamQuestion.query.filter_by(exam_id=exam.id).all()
        self.assertEqual(len(eqs), 10)

        for eq in eqs:
            q = Question.query.get(eq.question_id)
            orig_opts = {'A': q.option_a, 'B': q.option_b, 'C': q.option_c, 'D': q.option_d}
            orig_correct_text = orig_opts[q.correct_option]

            shuffled_opts = {
                'A': eq.get_option_a(),
                'B': eq.get_option_b(),
                'C': eq.get_option_c(),
                'D': eq.get_option_d()
            }
            remapped_correct_letter = eq.get_correct_option()

            # Verify the option corresponding to remapped_correct_letter holds the original correct text!
            self.assertEqual(shuffled_opts[remapped_correct_letter], orig_correct_text,
                             f"Remapped correct option '{remapped_correct_letter}' must match original correct text '{orig_correct_text}'")

    # 14. Scoring is correct
    def test_accurate_scoring(self):
        self.login_teacher()
        sub = Subject.query.filter_by(name='Maths').first()
        self.client.post(f'/teacher/create-exam/{sub.id}', data={
            'total_questions': 5,
            'duration': 10
        })

        exam = Exam.query.filter_by(subject_id=sub.id).first()
        eqs = ExamQuestion.query.filter_by(exam_id=exam.id).order_by(ExamQuestion.question_order).all()

        # Student registers
        self.client.post(f'/exam/{exam.exam_code}', data={
            'name': 'Test Student',
            'roll_number': 'ROLL-101',
            'branch': 'Computer Science'
        })
        student = Student.query.filter_by(roll_number='ROLL-101').first()

        # Submit 3 correct choices, 1 wrong choice, leave 1 unanswered
        submit_data = {}
        for idx, eq in enumerate(eqs):
            if idx < 3:
                submit_data[f'q_{eq.question_id}'] = eq.get_correct_option()
            elif idx == 3:
                # Wrong choice
                wrong_opt = 'A' if eq.get_correct_option() != 'A' else 'B'
                submit_data[f'q_{eq.question_id}'] = wrong_opt

        res = self.client.post(f'/exam/{exam.exam_code}/submit', data=submit_data, follow_redirects=True)
        self.assertEqual(res.status_code, 200)

        result = Result.query.filter_by(student_id=student.id).first()
        self.assertEqual(result.total_questions, 5)
        self.assertEqual(result.correct_answers, 3)
        self.assertEqual(result.wrong_answers, 1)
        self.assertEqual(result.unanswered, 1)
        self.assertEqual(result.marks_obtained, 3)
        self.assertEqual(result.percentage, 60.0)

    # 15. Question validator rejects invalid question data
    def test_question_validator_rejections(self):
        # Missing option
        invalid_q1 = {
            'question_text': 'Valid question text?',
            'option_a': 'Opt A',
            'option_b': 'Opt B',
            'option_c': '',
            'option_d': 'Opt D',
            'correct_option': 'A',
            'explanation': 'Some explanation',
            'subject': 'Grammar'
        }
        is_valid, err = validate_question_data(invalid_q1)
        self.assertFalse(is_valid)
        self.assertIn("4 non-empty options", err)

        # Invalid correct option
        invalid_q2 = {
            'question_text': 'Valid question text 2?',
            'option_a': 'Opt A',
            'option_b': 'Opt B',
            'option_c': 'Opt C',
            'option_d': 'Opt D',
            'correct_option': 'E',
            'explanation': 'Some explanation',
            'subject': 'Grammar'
        }
        is_valid, err = validate_question_data(invalid_q2)
        self.assertFalse(is_valid)
        self.assertIn("Invalid correct_option", err)

    # 16. Sequential Display Numbering (1-N) for 20 and 50 Question Exams
    def test_sequential_display_numbering_20_and_50_questions(self):
        self.login_teacher()
        sub = Subject.query.filter_by(name='Grammar').first()

        # Test 20 questions
        self.client.post(f'/teacher/create-exam/{sub.id}', data={'total_questions': 20, 'duration': 30})
        exam20 = Exam.query.order_by(Exam.id.desc()).first()
        eqs20 = ExamQuestion.query.filter_by(exam_id=exam20.id).order_by(ExamQuestion.question_order).all()
        self.assertEqual(len(eqs20), 20)
        orders20 = [eq.question_order for eq in eqs20]
        self.assertEqual(orders20, list(range(1, 21)), "20-question exam must have sequential orders 1 through 20")

        # Test 50 questions
        self.client.post(f'/teacher/create-exam/{sub.id}', data={'total_questions': 50, 'duration': 60})
        exam50 = Exam.query.order_by(Exam.id.desc()).first()
        eqs50 = ExamQuestion.query.filter_by(exam_id=exam50.id).order_by(ExamQuestion.question_order).all()
        self.assertEqual(len(eqs50), 50)
        orders50 = [eq.question_order for eq in eqs50]
        self.assertEqual(orders50, list(range(1, 51)), "50-question exam must have sequential orders 1 through 50")

    # 17. Multiple Exams Randomness & Unique Questions
    def test_multiple_exams_randomness(self):
        self.login_teacher()
        sub = Subject.query.filter_by(name='Physics').first()

        exam_q_sets = []
        for _ in range(3):
            self.client.post(f'/teacher/create-exam/{sub.id}', data={'total_questions': 15, 'duration': 20})
            exam = Exam.query.order_by(Exam.id.desc()).first()
            eqs = ExamQuestion.query.filter_by(exam_id=exam.id).order_by(ExamQuestion.question_order).all()
            q_ids = [eq.question_id for eq in eqs]
            
            # Verify no duplicates in single exam
            self.assertEqual(len(q_ids), len(set(q_ids)), "Each exam must contain unique question IDs")
            exam_q_sets.append(tuple(q_ids))

        # Verify not all 3 exams produced the identical list/order of questions
        self.assertTrue(len(set(exam_q_sets)) > 1, "Different exams should have randomized question selections/orders")

    # 18. Dashboard, Public Links, and Existing Functionality
    def test_teacher_dashboard_and_public_links(self):
        self.login_teacher()
        res = self.client.get('/teacher/dashboard')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Grammar', res.data)
        self.assertIn(b'Physics', res.data)
        self.assertIn(b'Chemistry', res.data)
        self.assertIn(b'Maths', res.data)

        # Create exam and open public link
        sub = Subject.query.filter_by(name='Grammar').first()
        self.client.post(f'/teacher/create-exam/{sub.id}', data={
            'total_questions': 5,
            'duration': 10
        })
        exam = Exam.query.first()
        res = self.client.get(f'/exam/{exam.exam_code}')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Enter Student Details', res.data)

if __name__ == '__main__':
    unittest.main()
