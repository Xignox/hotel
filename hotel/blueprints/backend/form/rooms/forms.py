from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, validators, TextAreaField,IntegerField,SelectField
from wtforms.validators import DataRequired, InputRequired, Email,Required

class RoomsForm(FlaskForm):					
	room_type = StringField('room types')
	status = StringField('Status')
	price = StringField('price')
	
	submit = SubmitField('Submit')

   