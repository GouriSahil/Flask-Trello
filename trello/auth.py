from flask_login import current_user
from wtforms import StringField , PasswordField , SubmitField
from flask_wtf import FlaskForm
from trello.models import User
from wtforms.validators import DataRequired , Email , Length, EqualTo, ValidationError

class RegestrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), ])
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('User already exist!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exist!')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')