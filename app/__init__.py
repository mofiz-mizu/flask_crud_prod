from flask import Flask
from app.config import Config
from app.extensions import db
from app.users.routes import bp
import time

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(bp)

    with app.app_context():
        for _ in range(10):
            try:
                db.create_all()
                break
            except Exception:
                time.sleep(2)

    return app
