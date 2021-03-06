import os
from flask import Flask
app = Flask(__name__)
import dj_database_url

from flask_sqlalchemy import SQLAlchemy

if os.environ.get("HEROKU"):
	app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
else:
	app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/forum.db"
	app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from app.include.classes.category import *
from app import views
from app.auth import models
from app.auth import views

from app.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager,current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


db.create_all()
