from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, FileField
from wtforms.validators import InputRequired, Email, DataRequired
import email_validator

class LoginForm(FlaskForm):
    username = TextField('Username', id='username_login', validators=[DataRequired()])
    password = PasswordField('Password', id='pwd_login', validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
    username = TextField('Username', id='username_create' , validators=[DataRequired()])
    email    = TextField('Email', id='email_create', validators=[DataRequired(), Email()])
    password = PasswordField('Password', id='pwd_create', validators=[DataRequired()])