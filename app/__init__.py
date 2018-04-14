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

db.create_all()
