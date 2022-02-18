from flask import Flask
from app.user import user

def creat_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    app.register_blueprint(user, url_prefix='/user')

    return app
