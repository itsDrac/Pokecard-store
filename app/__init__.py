from flask import Flask

def creat_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    
    return app
