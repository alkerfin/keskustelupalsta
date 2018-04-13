import os
from flask import Flask
app = Flask(__name__)
import dj_database_url

from flask_sqlalchemy import SQLAlchemy
if os.environ['DATABASE_URL'] is None:
	app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://acgzltixozxxpe:05a6cc8342b1a562eab32a1020d523a4b5ac50ded83fe1e1977741c4ecfccc2a@ec2-54-247-111-19.eu-west-1.compute.amazonaws.com:5432/ddqluf38h1mj3l"
else:
	app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from app.include.classes.category import *
from app import views
from app.auth import models

db.create_all()
