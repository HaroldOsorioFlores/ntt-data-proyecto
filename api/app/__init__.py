from flask import Flask
from app.models import db
from app.routes import main

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app