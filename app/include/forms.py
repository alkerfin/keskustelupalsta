from flask_wtf import FlaskForm
from wtform import StringField, validators

class CategoryForm(FlaskForm):
	name = StringField("Kategorian nimi",[validators.Length(min=2)])
	description = StringField("Kategorian kuvaus")

	
	
	class Meta:
		csrf = False

