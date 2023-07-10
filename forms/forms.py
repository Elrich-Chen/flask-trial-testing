from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import Length, input_required, EqualTo, Email, email_validator

class RegistrationForm(FlaskForm):
    username = StringField ('Username', 
        validators=[input_required(), Length(min=2, max=20)])
    email = StringField('Email',
        validators=[input_required(), Email("Enter")])
    password = StringField('Password', validators=[input_required()])
    confirm_password= StringField('Confirm Password', 
        validators = [input_required(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[input_required(), Email("Enter")])
    password = StringField('Password', validators=[input_required()])
    remember = BooleanField('remember me')
    submit = SubmitField('Login')
    