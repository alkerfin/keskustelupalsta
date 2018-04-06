from flask_wtf import FlaskForm
from wtform import StringField

class CategoryForm(FlaskForm):
	name = StringField("Kategorian nimi")
	description = StringField("Kategorian kuvaus")

	class Meta:
		csrf = False
