from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, DateTimeField, BooleanField, SubmitField, SelectField, DateField, validators, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length , Email, NumberRange,Required
from extension import db


class LoginForm(FlaskForm):
    email = StringField(('Email'), validators=[Required(('Email is required')),
        validators.Email(('Invalid Email Address'))])
    password = PasswordField(('Password'), validators=[Required(('Password mo! required')),
        validators.DataRequired(('Invalid Password'))])
    submit = SubmitField('Sign In')
