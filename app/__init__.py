from flask import Flask
from app.extinsions import db, login_manager
from app.user import user

def creat_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(user, url_prefix='/user')

    return app
