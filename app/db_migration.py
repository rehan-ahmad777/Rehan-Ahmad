import uuid
import random
import string
from datetime import datetime
from sqlalchemy import inspect, text
from app.extensions import db

def generate_unique_code(existing_codes):
    chars = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(random.choices(chars, k=6))
        if code not in existing_codes:
            existing_codes.add(code)
            return code

def init_and_migrate_db(app):
    """
    Ensures all database tables exist and performs safe, non-destructive
    schema migration to add any missing columns (e.g. exam_code, exam_token)
    to existing production databases (Render PostgreSQL / MySQL / SQLite).
    """
    with app.app_context():
        # First, ensure base tables exist
        db.create_all()

        try:
            engine = db.engine
            inspector = inspect(engine)
            existing_tables = inspector.get_table_names()

            if 'exams' in existing_tables:
                columns_info = inspector.get_columns('exams')
                existing_columns = {c['name']: c for c in columns_info}

                dialect = engine.dialect.name.lower()

                # Add exam_code if missing
                if 'exam_code' not in existing_columns:
                    col_type = 'VARCHAR(20)'
                    with engine.connect() as conn:
                        conn.execute(text(f"ALTER TABLE exams ADD COLUMN exam_code {col_type}"))
                        if dialect != 'sqlite':
                            conn.commit()

                # Add exam_token if missing
                if 'exam_token' not in existing_columns:
                    col_type = 'VARCHAR(64)'
                    with engine.connect() as conn:
                        conn.execute(text(f"ALTER TABLE exams ADD COLUMN exam_token {col_type}"))
                        if dialect != 'sqlite':
                            conn.commit()

                # Add expires_at if missing
                if 'expires_at' not in existing_columns:
                    col_type = 'TIMESTAMP' if 'postgres' in dialect else 'DATETIME'
                    with engine.connect() as conn:
                        conn.execute(text(f"ALTER TABLE exams ADD COLUMN expires_at {col_type}"))
                        if dialect != 'sqlite':
                            conn.commit()

                # Add status if missing
                if 'status' not in existing_columns:
                    col_type = "VARCHAR(20) DEFAULT 'active'"
                    with engine.connect() as conn:
                        conn.execute(text(f"ALTER TABLE exams ADD COLUMN status {col_type}"))
                        if dialect != 'sqlite':
                            conn.commit()

                # Backfill any existing exam rows that have NULL or empty exam_code or exam_token
                from app.models.exam import Exam
                exams_to_fix = Exam.query.all()
                if exams_to_fix:
                    existing_codes = set(e.exam_code for e in exams_to_fix if e.exam_code)
                    existing_tokens = set(e.exam_token for e in exams_to_fix if e.exam_token)

                    fixed = False
                    for exam in exams_to_fix:
                        if not exam.exam_code:
                            exam.exam_code = generate_unique_code(existing_codes)
                            fixed = True
                        if not exam.exam_token:
                            token = uuid.uuid4().hex
                            while token in existing_tokens:
                                token = uuid.uuid4().hex
                            existing_tokens.add(token)
                            exam.exam_token = token
                            fixed = True
                        if not exam.status:
                            exam.status = 'active'
                            fixed = True

                    if fixed:
                        db.session.commit()

        except Exception as e:
            app.logger.warning(f"Schema migration check completed with info/notice: {e}")
