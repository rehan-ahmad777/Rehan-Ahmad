import os
from app import create_app
from app.extensions import db
from database.seed_questions import seed_database

debug_mode = os.getenv('FLASK_DEBUG', '1') in ('1', 'true', 'True')
env_name = 'development' if debug_mode else 'production'
app = create_app(env_name)

# Ensure database tables exist & seed on startup
with app.app_context():
    db.create_all()
    # If no subjects exist, seed initial question bank and teacher
    from app.models.subject import Subject
    if Subject.query.count() == 0:
        print("Empty database detected. Running question bank seeder...")
        seed_database()

if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    print(f"Starting Online AI Quiz System server at http://{host}:{port}")
    app.run(host=host, port=port, debug=(env_name == 'development'))
