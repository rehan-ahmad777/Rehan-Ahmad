# Online AI Quiz / Examination System

A complete, professional, production-ready **Online AI Quiz / Examination System** built with **Python (Flask)**, **MySQL / SQLAlchemy ORM**, **Bootstrap 5**, **JavaScript**, and **Chart.js**.

---

## 🌟 Key Features

### 1. Multi-Role Authorization & Security
- **Teacher Login**: Secure authentication powered by `Werkzeug` password hashing and `Flask-Login`.
- **Student Exam Link**: Unique UUID4 tokenized URLs (e.g. `/exam/<secure-token>`). Database IDs are never exposed.
- **Strict Authorization**: Teachers can ONLY view their own created exam papers and candidate scores. Students can ONLY view their own scorecards via session validation.

### 2. Random & Fixed Question Paper Generator
- **Subject Bank**: 4 subjects (**Grammar**, **Physics**, **Chemistry**, **Mathematics**) seeded with **100 MCQs each** (400 total questions).
- **Server-Side Random Selection**: Randomly picks N questions from the subject bank when creating the exam.
- **Fixed Exam Paper**: Once created, the questions are **permanently frozen** inside `exam_questions` preserving order. All students using the same exam link receive the exact same question paper.

### 3. Student Examination & Live Countdown Timer
- **No Account Required**: Students enter compulsory details (Name, Roll Number, Branch) and immediately begin the exam.
- **Interactive UI**: Question palette navigation, answered/unanswered indicators, option selection tiles, and confirmation modal.
- **Server-Side Timer Enforcement**: Real-time JavaScript countdown timer synchronized with backend timestamp validation (`started_at + duration`). Automatically submits and locks attempt upon expiry.
- **Duplicate Submission Lockout**: Re-submitting an already completed attempt is strictly prevented.

### 4. Automated Grading & Real-Time Analytics
- **Server-Side Grading Only**: Marks (+1 correct, 0 wrong/unanswered) are calculated exclusively on the Flask backend. Client marks are never trusted.
- **Question-Wise Review**: Displays student's choice vs correct option key with status badges.
- **Teacher Analytics**: Interactive class performance bar charts and pass/fail doughnut charts powered by **Chart.js**, along with search, branch filter, and score sorting.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.7+, Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF, Flask-Limiter
- **Database**: MySQL (PyMySQL driver) with SQLAlchemy ORM (includes SQLite fallback option for lightweight testing)
- **Frontend**: HTML5, CSS3 (Modern Glassmorphism & Custom Responsive Design), JavaScript (ES6+ AJAX Fetch API), Bootstrap 5, Chart.js

---

## 📂 Project Structure

```text
online_ai_quiz/
├── app/
│   ├── __init__.py          # Flask app factory, extension setup & error handlers
│   ├── extensions.py        # SQLAlchemy, LoginManager, CSRFProtect, Limiter instances
│   ├── models/
│   │   ├── __init__.py
│   │   ├── teacher.py       # Teacher model with password hashing
│   │   ├── subject.py       # Subject model
│   │   ├── question.py      # Question model (Question Bank)
│   │   ├── exam.py          # Exam & ExamQuestion models
│   │   └── student.py       # Student, StudentAnswer & Result models
│   ├── auth/
│   │   └── routes.py        # Teacher login / logout endpoints
│   ├── teacher/
│   │   └── routes.py        # Teacher dashboard, exam generator, class results
│   ├── student/
│   │   └── routes.py        # Token URL validation & student registration form
│   ├── exam/
│   │   └── routes.py        # Active test session, AJAX answer saver & evaluation
│   ├── templates/
│   │   ├── base.html        # Shared navigation layout
│   │   ├── index.html       # Landing page
│   │   ├── auth/            # Login template
│   │   ├── teacher/         # Dashboard, create exam, exam created & results templates
│   │   ├── student/         # Student register, take exam & scorecard templates
│   │   └── errors/          # 403, 404, 500 & exam_expired templates
│   └── static/
│       ├── css/style.css    # Modern UI styles, glassmorphic navbar, option tiles
│       └── js/              # Client-side scripts
├── database/
│   └── seed_questions.py    # Populates 400 questions (100 per subject) & teacher account
├── config.py                # App configuration profiles
├── run.py                   # App entrypoint
├── requirements.txt         # Dependencies
├── .env.example             # Environment variable template
├── .env                     # Local environment variables
└── tests/
    └── test_quiz_system.py  # Pytest automated test suite
```

---

## 🚀 Quick Setup & Installation

### 1. Clone / Open Project Directory
```bash
cd "d:/my quize protol"
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables (`.env`)
Create or edit `.env` in the root directory:
```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=9f8a7b6c5d4e3f2a1b0c9d8e7f6a5b4c

# MySQL Credentials
DB_USER=root
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=online_quiz_db

# Fallback to local SQLite file if MySQL service is not running
USE_SQLITE_FALLBACK=True
```

### 4. MySQL Setup (Optional for local MySQL server)
Create the MySQL database:
```sql
CREATE DATABASE online_quiz_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 5. Seed Database (Populate 400 Questions + Teacher)
```bash
python database/seed_questions.py
```

---

## 🔑 Default Seed Credentials

- **Teacher ID**: `T1001`
- **Password**: `Teacher@123`

---

## 🏃 Running the Application

Start the Flask development server:
```bash
python run.py
```
Open your browser at: `http://127.0.0.1:5000`

---

## 🧪 Running Automated Tests

Execute the Pytest test suite:
```bash
python -m pytest tests/test_quiz_system.py -v
```

All 9 test cases cover authentication, paper generation, question order freezing, registration validation, server-side grading accuracy, duplicate submission lockout, and teacher/student authorization checks.

---

## 🌐 Deploying to Render

### 1. Create a New Web Service on Render
1. Connect your Git repository to [Render](https://render.com).
2. Click **New +** -> **Web Service**.
3. Select Runtime: **Python**.

### 2. Render Deployment Commands

* **Build Command**:
  ```bash
  pip install -r requirements.txt
  ```

* **Start Command**:
  ```bash
  gunicorn --bind 0.0.0.0:$PORT run:app
  ```

### 3. Required Render Environment Variables

Configure the following variables under **Environment Variables** in your Render service dashboard:

| Environment Variable | Value | Description |
| :--- | :--- | :--- |
| `FLASK_APP` | `run.py` | Application entrypoint |
| `FLASK_DEBUG` | `0` | Production mode (debug disabled) |
| `SECRET_KEY` | `your-random-production-secret-key` | Production session signing key |
| `DATABASE_URL` | *(Auto-populated by Render PostgreSQL)* | PostgreSQL connection URI |

*(Note: Render automatically populates `DATABASE_URL` when you create and link an Internal PostgreSQL database to your web service).*

