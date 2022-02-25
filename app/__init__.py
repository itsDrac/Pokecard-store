from flask import Flask
from app.extinsions import db, login_manager, admin as administrator
from app.user import user_bp
from app.admin import admin

def creat_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    login_manager.init_app(app)
    administrator.init_app(app)

    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(admin)

    return app
