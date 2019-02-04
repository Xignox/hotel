from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, validators, TextAreaField,IntegerField,SelectField
from wtforms.validators import DataRequired, InputRequired, Email,Required


class ReservationForm(FlaskForm):
    users_id = StringField('users_id')
    rooms_id = StringField('rooms_id')
    date_in = StringField('date_in')
    date_out = StringField('date_out')
    child_count = StringField('discount')
    adult_count = StringField('adult_count')
    submit = SubmitField('Submit')