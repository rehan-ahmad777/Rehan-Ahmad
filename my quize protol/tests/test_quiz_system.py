import unittest
import os
import sys
from datetime import datetime, timedelta

# Path setup
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.extensions import db
from app.models import Teacher, Subject, Question, Exam, ExamQuestion, Student, StudentAnswer, Result
from app.exam.routes import process_and_finalize_submission

class QuizSystemTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test environment and in-memory database."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.drop_all()
        db.create_all()

        # Seed initial data
        self.seed_test_data()

    def tearDown(self):
        """Tear down test database."""
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def seed_test_data(self):
        # Create Teacher
        self.teacher = Teacher(teacher_id='T1001', name='Dr. Test Teacher')
        self.teacher.set_password('Password123!')
        db.session.add(self.teacher)

        # Create Subject
        self.subject = Subject(name='Physics')
        db.session.add(self.subject)
        db.session.flush()

        # Create 20 Questions for Physics
        self.questions = []
        for i in range(1, 21):
            q = Question(
                subject_id=self.subject.id,
                question_text=f"Sample Question {i}?",
                option_a=f"Option A{i}",
                option_b=f"Option B{i}",
                option_c=f"Option C{i}",
                option_d=f"Option D{i}",
                correct_option='A' if i % 2 == 1 else 'B'
            )
            db.session.add(q)
            self.questions.append(q)

        db.session.commit()

    # 1. AUTHENTICATION TESTS
    def test_teacher_login_success(self):
        response = self.client.post('/auth/login', data={
            'teacher_id': 'T1001',
            'password': 'Password123!'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome back, Dr. Test Teacher!', response.data)

    def test_teacher_login_failure(self):
        response = self.client.post('/auth/login', data={
            'teacher_id': 'T1001',
            'password': 'WrongPassword'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid Teacher ID or Password', response.data)

    def test_password_hashing(self):
        self.assertTrue(self.teacher.check_password('Password123!'))
        self.assertFalse(self.teacher.check_password('WrongPassword'))
        self.assertNotEqual(self.teacher.password_hash, 'Password123!')

    # 2. EXAM CREATION TESTS
    def test_create_exam_paper(self):
        # Login first
        self.client.post('/auth/login', data={'teacher_id': 'T1001', 'password': 'Password123!'})

        response = self.client.post(f'/teacher/create-exam/{self.subject.id}', data={
            'total_questions': '10',
            'duration': '15'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Question Paper Successfully Generated!', response.data)

        # Verify DB exam record
        exam = Exam.query.filter_by(subject_id=self.subject.id).first()
        self.assertIsNotNone(exam)
        self.assertEqual(exam.total_questions, 10)
        self.assertEqual(exam.total_marks, 10)
        self.assertEqual(exam.duration, 15)

        # Verify exact 10 questions assigned without duplicates
        eqs = ExamQuestion.query.filter_by(exam_id=exam.id).all()
        self.assertEqual(len(eqs), 10)
        
        q_ids = [eq.question_id for eq in eqs]
        self.assertEqual(len(q_ids), len(set(q_ids)), "Exam questions must be unique without duplicates")

    def test_invalid_exam_question_count(self):
        self.client.post('/auth/login', data={'teacher_id': 'T1001', 'password': 'Password123!'})

        # Exceed available 20 questions
        response = self.client.post(f'/teacher/create-exam/{self.subject.id}', data={
            'total_questions': '50',
            'duration': '15'
        }, follow_redirects=True)

        self.assertIn(b'Cannot select 50 questions', response.data)

    # 3. STUDENT REGISTRATION & EXAM SESSION TESTS
    def test_student_registration_mandatory_fields(self):
        exam = Exam(
            subject_id=self.subject.id,
            teacher_id=self.teacher.id,
            exam_code='EXAM-TEST1',
            exam_token='test-token-12345',
            total_questions=5,
            total_marks=5,
            duration=10,
            status='active'
        )
        db.session.add(exam)
        db.session.commit()

        # Missing branch field
        response = self.client.post(f'/exam/{exam.exam_token}', data={
            'name': 'Alice Smith',
            'roll_number': '101',
            'branch': ''
        }, follow_redirects=True)

        self.assertIn(b'All fields (Name, Roll Number, Branch) are strictly compulsory', response.data)

    # 4. SERVER-SIDE EVALUATION & GRADING ACCURACY TESTS
    def test_automated_result_grading(self):
        exam = Exam(
            subject_id=self.subject.id,
            teacher_id=self.teacher.id,
            exam_code='EXAM-GRAD1',
            exam_token='grade-token-555',
            total_questions=4,
            total_marks=4,
            duration=20,
            status='active'
        )
        db.session.add(exam)
        db.session.flush()

        # Assign 4 specific questions
        q_sample = self.questions[:4]
        for order, q in enumerate(q_sample, start=1):
            eq = ExamQuestion(exam_id=exam.id, question_id=q.id, question_order=order)
            db.session.add(eq)

        student = Student(
            exam_id=exam.id,
            name='Bob Johnson',
            roll_number='202',
            branch='Computer Science',
            started_at=datetime.utcnow()
        )
        db.session.add(student)
        db.session.commit()

        # Mock student choices: 2 correct, 1 wrong, 1 unanswered
        # Q1 correct_option='A', choice='A' (Correct)
        # Q2 correct_option='B', choice='A' (Wrong)
        # Q3 correct_option='A', choice='A' (Correct)
        # Q4 correct_option='B', choice=None (Unanswered)
        db.session.add(StudentAnswer(student_id=student.id, question_id=q_sample[0].id, selected_option='A'))
        db.session.add(StudentAnswer(student_id=student.id, question_id=q_sample[1].id, selected_option='A'))
        db.session.add(StudentAnswer(student_id=student.id, question_id=q_sample[2].id, selected_option='A'))
        db.session.commit()

        # Trigger backend evaluation
        result = process_and_finalize_submission(student, exam)

        self.assertEqual(result.total_questions, 4)
        self.assertEqual(result.correct_answers, 2)
        self.assertEqual(result.wrong_answers, 1)
        self.assertEqual(result.unanswered, 1)
        self.assertEqual(result.marks_obtained, 2) # 2 / 4 marks
        self.assertEqual(result.percentage, 50.0)

    # 5. SECURITY & AUTHORIZATION TESTS
    def test_duplicate_submission_lockout(self):
        exam = Exam(
            subject_id=self.subject.id,
            teacher_id=self.teacher.id,
            exam_code='EXAM-LOCK',
            exam_token='lock-token-777',
            total_questions=2,
            total_marks=2,
            duration=10,
            status='active'
        )
        db.session.add(exam)
        db.session.flush()

        student = Student(
            exam_id=exam.id,
            name='Charlie Brown',
            roll_number='303',
            branch='IT',
            started_at=datetime.utcnow(),
            submitted_at=datetime.utcnow()
        )
        db.session.add(student)
        db.session.commit()

        # Try registering again with same roll number
        response = self.client.post(f'/exam/{exam.exam_token}', data={
            'name': 'Charlie Brown',
            'roll_number': '303',
            'branch': 'IT'
        }, follow_redirects=True)

        self.assertIn(b'has already completed and submitted this exam', response.data)

    def test_unauthorized_result_access(self):
        exam = Exam(
            subject_id=self.subject.id,
            teacher_id=self.teacher.id,
            exam_code='EXAM-AUTH',
            exam_token='auth-token-999',
            total_questions=2,
            total_marks=2,
            duration=10,
            status='active'
        )
        db.session.add(exam)
        db.session.flush()

        student = Student(exam_id=exam.id, name='Eve', roll_number='404', branch='ECE')
        db.session.add(student)
        db.session.flush()

        result = Result(
            student_id=student.id,
            exam_id=exam.id,
            total_questions=2,
            correct_answers=2,
            wrong_answers=0,
            unanswered=0,
            marks_obtained=2,
            percentage=100.0
        )
        db.session.add(result)
        db.session.commit()

        # Access result without active student session or teacher login
        response = self.client.get(f'/exam/result/{student.id}')
        self.assertEqual(response.status_code, 403)

if __name__ == '__main__':
    unittest.main()
