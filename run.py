import os
from app import create_app
from app.extensions import db
from database.seed_questions import seed_database

debug_mode = os.getenv('FLASK_DEBUG', '0') in ('1', 'true', 'True')
env_name = 'development' if debug_mode else 'production'
app = create_app(env_name)

# Ensure database tables exist & seed only when DB is empty
with app.app_context():
    db.create_all()
    from app.models.subject import Subject
    from app.models.question import Question
    if Subject.query.count() == 0 or Question.query.count() == 0:
        print("Empty database or missing questions detected. Seeding initial 400 question bank...")
        seed_database(app=app, force_reseed=False)

import socket

def get_lan_ips():
    ips = set()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ips.add(s.getsockname()[0])
        s.close()
    except Exception:
        pass
    try:
        hostname = socket.gethostname()
        for ip in socket.gethostbyname_ex(hostname)[2]:
            if not ip.startswith("127."):
                ips.add(ip)
    except Exception:
        pass
    return sorted(list(ips))

if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('PORT', os.getenv('FLASK_PORT', 5000)))

    lan_ips = get_lan_ips()
    primary_lan = lan_ips[0] if lan_ips else '127.0.0.1'

    print("\n" + "="*70)
    print(" ONLINE AI QUIZ SYSTEM IS NOW RUNNING!")
    print("="*70)
    print(f" ACCESS ON THIS COMPUTER (PC):")
    print(f"    -> http://localhost:{port}")
    print(f"    -> http://127.0.0.1:{port}")
    print("-" * 70)
    print(f" ACCESS ON MOBILE / ANOTHER DEVICE (Same Wi-Fi / Hotspot):")
    if lan_ips:
        for ip in lan_ips:
            print(f"    -> http://{ip}:{port}")
    else:
        print(f"    -> http://<YOUR_COMPUTER_IP>:{port}")
    print("-" * 70)
    print(" INSTRUCTIONS FOR ANOTHER DEVICE / MOBILE:")
    print("    1. Connect your phone or other device to the SAME Wi-Fi / Hotspot.")
    print(f"    2. Open browser on your device & enter: http://{primary_lan}:{port}")
    print("="*70 + "\n")

    app.run(host=host, port=port, debug=(env_name == 'development'))
