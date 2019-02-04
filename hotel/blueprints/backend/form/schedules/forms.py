from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, validators, TextAreaField,IntegerField,SelectField
from wtforms.validators import DataRequired, InputRequired, Email,Required


class ScheduleForm(FlaskForm):
    driver_id = StringField('Driver')
    bus_id = StringField('Bus')
    conductor_id = StringField('Conductor')
    departured_at = StringField(validators=[Required(message="Please Enter Departured Date")])
    arrived_at = StringField('Arrived')
    origin = StringField('Origin')
    destination = SubmitField('Destination')