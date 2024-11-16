from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SignupForm(FlaskForm):
    first_name = StringField('First_name',
                             validators=[DataRequired(), Length(max=20,message = "Chater limit reached")])
    last_name = StringField('Last_name', 
                            validators=[DataRequired(), Length(max=20,message = "Chater limit reached")])
    email = StringField('Email', 
                       validators=[DataRequired(),Email()])
    device_id = StringField('Device ID',
                            validators=[DataRequired(), Length(min=8, max=8, message="Incorrect device ID")])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', 
                       validators=[DataRequired(),Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')