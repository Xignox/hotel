from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, validators, TextAreaField,IntegerField,SelectField
from wtforms.validators import DataRequired, InputRequired, Email,Required


class RoleForm(FlaskForm):
    name = StringField(validators=[Required(message="Please Enter Firstname")])
    description = StringField('Description',)
    submit = SubmitField('Submit')