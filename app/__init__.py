import os
from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from app.include.classes.category import *
from app import views
from app.auth import models

db.create_all()
