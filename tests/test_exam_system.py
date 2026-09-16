import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app import create_app
from app.extensions import db
from app.models import Teacher, Subject, Question, Exam, ExamQuestion, Student, StudentAnswer, Result

class ExamSystemTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        db.create_all()

        # Seed test teacher
        self.teacher = Teacher(teacher_id='T1001', name='Dr. Alan Turing')
        self.teacher.set_password('Teacher@123')
        db.session.add(self.teacher)

        # Seed test subject & questions
        self.subject = Subject(name='Physics')
        db.session.add(self.subject)
        db.session.flush()

        for i in range(1, 26):
            q = Question(
                subject_id=self.subject.id,
                question_text=f'Physics Question {i} text?',
                option_a='Option A',
                option_b='Option B',
                option_c='Option C',
                option_d='Option D',
                correct_option='A'
            )
            db.session.add(q)

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def login_teacher(self):
        return self.client.post('/auth/login', data={
            'teacher_id': 'T1001',
            'password': 'Teacher@123'
        }, follow_redirects=True)

    def test_complete_exam_flow(self):
        # 1 & 2. Teacher Login
        res = self.login_teacher()
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Welcome, Dr. Alan Turing', res.data)

        # 3. Open Teacher Dashboard
        res = self.client.get('/teacher/dashboard')
        self.assertEqual(res.status_code, 200)

        # 4 & 5. Create Physics Exam with 20 marks
        res = self.client.post(f'/teacher/create-exam/{self.subject.id}', data={
            'total_questions': 20,
            'duration': 30
        }, follow_redirects=True)
        self.assertEqual(res.status_code, 200)

        # 6, 7, 8, 9, 10. Verify Exam created in DB with 20 questions
        exam = Exam.query.filter_by(subject_id=self.subject.id).first()
        self.assertIsNotNone(exam)
        self.assertEqual(exam.total_questions, 20)
        self.assertEqual(exam.total_marks, 20)
        self.assertEqual(len(exam.exam_code), 6) # Unique 6-char code

        # Check locked questions count
        eq_count = ExamQuestion.query.filter_by(exam_id=exam.id).count()
        self.assertEqual(eq_count, 20)

        # 12. Student Opens Exam Link using code /exam/EXAM_CODE
        res = self.client.get(f'/exam/{exam.exam_code}')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Physics', res.data)

        # 13, 14, 15, 16. Student Registers Details and Starts Exam
        res = self.client.post(f'/exam/{exam.exam_code}', data={
            'name': 'Rehan Ahmad',
            'roll_number': '2026-CS-001',
            'branch': 'Computer Science & Engineering'
        }, follow_redirects=True)
        self.assertEqual(res.status_code, 200)

        student = Student.query.filter_by(roll_number='2026-CS-001').first()
        self.assertIsNotNone(student)

        # 17 & 18. Student Submits Answers
        # Submit all 20 questions with their correct shuffled option choice
        eq_records = ExamQuestion.query.filter_by(exam_id=exam.id).order_by(ExamQuestion.question_order).all()
        submit_data = {}
        for eq in eq_records:
            submit_data[f'q_{eq.question_id}'] = eq.get_correct_option()

        res = self.client.post(f'/exam/{exam.exam_code}/submit', data=submit_data, follow_redirects=True)
        self.assertEqual(res.status_code, 200)

        # 19, 20, 21. Automatic Result Calculation
        result = Result.query.filter_by(student_id=student.id).first()
        self.assertIsNotNone(result)
        self.assertEqual(result.marks_obtained, 20)
        self.assertEqual(result.correct_answers, 20)
        self.assertEqual(result.percentage, 100.0)

        # 22 & 23. Teacher Views Results
        res = self.client.get('/teacher/results')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Rehan Ahmad', res.data)
        self.assertIn(b'2026-CS-001', res.data)

    def test_insufficient_questions_error(self):
        self.login_teacher()
        # Request 50 questions when only 25 exist in DB
        res = self.client.post(f'/teacher/create-exam/{self.subject.id}', data={
            'total_questions': 50,
            'duration': 30
        })
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Only 25 questions are available for Physics. Please enter a smaller number.', res.data)

        # Ensure no exam was created
        exam_count = Exam.query.count()
        self.assertEqual(exam_count, 0)

    def test_disable_exam(self):
        self.login_teacher()
        # Create exam
        self.client.post(f'/teacher/create-exam/{self.subject.id}', data={
            'total_questions': 10,
            'duration': 15
        })
        exam = Exam.query.first()
        self.assertEqual(exam.status, 'active')

        # Disable exam
        self.client.get(f'/teacher/exam/{exam.id}/disable', follow_redirects=True)
        exam_updated = Exam.query.get(exam.id)
        self.assertEqual(exam_updated.status, 'disabled')

        # Student opens disabled exam
        res = self.client.get(f'/exam/{exam.exam_code}')
        self.assertEqual(res.status_code, 403)
        self.assertIn(b'This exam is no longer available.', res.data)

    def test_render_public_url_generation(self):
        self.login_teacher()
        self.client.post(f'/teacher/create-exam/{self.subject.id}', data={
            'total_questions': 5,
            'duration': 15
        }, follow_redirects=True)
        exam = Exam.query.first()
        
        # Test with Render request headers
        res = self.client.get(
            f'/teacher/exam/{exam.exam_token}/created',
            headers={'X-Forwarded-Proto': 'https', 'Host': 'rehan-ahmad-1.onrender.com'}
        )
        self.assertEqual(res.status_code, 200)
        expected_url = f"https://rehan-ahmad-1.onrender.com/exam/{exam.exam_code}"
        self.assertIn(expected_url.encode('utf-8'), res.data)

    def test_valid_public_exam_code_opens_student_registration(self):
        self.login_teacher()
        self.client.post(f'/teacher/create-exam/{self.subject.id}', data={
            'total_questions': 5,
            'duration': 15
        })
        exam = Exam.query.first()
        
        # Unauthenticated student opens /exam/<exam_code>
        self.client.get('/auth/logout')
        res = self.client.get(f'/exam/{exam.exam_code}')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Enter Student Details', res.data)
        self.assertIn(b'Physics', res.data)

    def test_invalid_exam_code_returns_404(self):
        res = self.client.get('/exam/INVALID99')
        self.assertEqual(res.status_code, 404)
        self.assertIn(b'404 Page Not Found', res.data)

    def test_public_exam_route_never_redirects_to_teacher_dashboard(self):
        self.login_teacher()
        self.client.post(f'/teacher/create-exam/{self.subject.id}', data={
            'total_questions': 5,
            'duration': 15
        })
        exam = Exam.query.first()
        self.client.get('/auth/logout')

        # GET request without login must return 200 student page, not 302 redirect
        res = self.client.get(f'/exam/{exam.exam_code}', follow_redirects=False)
        self.assertEqual(res.status_code, 200)
        self.assertNotIn('location', res.headers)

    def test_case_insensitive_exam_code_lookup(self):
        self.login_teacher()
        self.client.post(f'/teacher/create-exam/{self.subject.id}', data={
            'total_questions': 5,
            'duration': 15
        })
        exam = Exam.query.first()
        self.client.get('/auth/logout')

        # Lowercase test
        res_lower = self.client.get(f'/exam/{exam.exam_code.lower()}')
        self.assertEqual(res_lower.status_code, 200)
        self.assertIn(b'Physics', res_lower.data)

        # Uppercase test
        res_upper = self.client.get(f'/exam/{exam.exam_code.upper()}')
        self.assertEqual(res_upper.status_code, 200)

    def test_end_to_end_teacher_creation_and_public_link_resolution(self):
        # 1. Teacher Logs in
        self.login_teacher()

        # 2. Teacher creates exam
        res_create = self.client.post(f'/teacher/create-exam/{self.subject.id}', data={
            'total_questions': 10,
            'duration': 20
        }, follow_redirects=True)
        self.assertEqual(res_create.status_code, 200)

        # 3. Verify exam record in DB
        exam = Exam.query.filter_by(subject_id=self.subject.id).first()
        self.assertIsNotNone(exam)
        self.assertIsNotNone(exam.exam_code)
        self.assertEqual(len(exam.exam_code), 6)

        # 4. Logout teacher to simulate unauthenticated student
        self.client.get('/auth/logout')

        # 5. Open GET /exam/<exam_code>
        res_public = self.client.get(f'/exam/{exam.exam_code}')
        self.assertEqual(res_public.status_code, 200)
        self.assertIn(b'Enter Student Details', res_public.data)
        self.assertIn(b'Physics', res_public.data)


if __name__ == '__main__':
    unittest.main()
