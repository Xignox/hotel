from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, validators, TextAreaField,IntegerField,SelectField
from wtforms.validators import DataRequired, InputRequired, Email,Required, Length


class UserForm(FlaskForm):
    firstname = StringField(validators=[Required(message="Please Enter Firstname")])
    lastname = StringField(validators=[Required(message="Please Enter Lastname")])
    middlename = StringField(validators=[Required(message="Please Enter Middlename")])
    address = StringField(validators=[Required(message="Please Enter Address")])
    mobile = StringField(validators=[Required(message="Mobile number exceed in 11 numbers") ,Length(min=10, max=11)])
    role = StringField(validators=[Required(message="Please Enter Role")])
    email = StringField(validators=[Required(message="Please Enter Email")])
    password = PasswordField('Password', validators=[Required(), Length(min=6, max=20)])
    confirm = PasswordField(validators=[Required(message="Please Enter Password")])
   
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    search = StringField('Search')
    submit = SubmitField('Submit')