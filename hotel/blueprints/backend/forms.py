from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, validators, TextAreaField,TextField
from wtforms.validators import DataRequired, InputRequired
from extension import db


class UserForm(FlaskForm):
    firstname = TextField('Name:', validators=[validators.required(), validators.Length(min=6, max=35)])
    lastname = TextField('Lastname',validators=[validators.required(), validators.Length(min=6, max=35)])
    middlename = StringField('Middlename')
    birthdate = StringField('Birthday')
    address = StringField('Address')
    phone = StringField('Phone')
    mobile = StringField('Mobile')
    email = StringField('Email Addrerss')
    license = StringField('License')
    submit = SubmitField('Submit')


