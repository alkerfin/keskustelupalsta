from flask_wtf import FlaskForm
from wtform import StringField

class CategoryForm(FlaskForm):
	name = StringField("Kategorian nimi")
	description = StringField("Kategorian kuvaus")

	class Meta:
		csrf = False

class WriteTopic(FlaskForm):
	topic = StringField("Otsikko")
	body = StringField("Viesti")


	class Meta:
		csrf = False

class WriteMessage(FlaskForm):
	topic = StringField("Otsikko")
	body = StringField("Viesti")
	
	class Meta:
		csrf = False
