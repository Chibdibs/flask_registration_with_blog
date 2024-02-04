"""
Author: Nino Ross
Class: SDEV 300

This is lab assignment 8 for SDEV 300. This is the __init__
for the Flask application.
"""

from os import path
from flask import Flask
from flask_login import LoginManager

from .views import views
from .models import Users, db

# DB_NAME = "database.db"


def create_app():
    """ This method initializes the Flask app that is run app.py """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    db.init_app(app)

    app.register_blueprint(views, url_prefix="/")

    with app.app_context():
        if not path.exists("instance/users.db"):
            db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = "views.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    return app
