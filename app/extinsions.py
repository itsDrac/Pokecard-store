from flask_mongoengine import MongoEngine
from flask_login import LoginManager

db = MongoEngine()
login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.login_message = "Please Login to access this page"
login_manager.login_message_category = "warning"
