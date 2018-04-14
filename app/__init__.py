import os
from flask import Flask
app = Flask(__name__)
import dj_database_url

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from app.include.classes.category import *
from app import views
from app.auth import models

db.create_all()
