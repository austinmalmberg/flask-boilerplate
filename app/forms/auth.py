
from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, EqualTo, Length, Email


class LoginForm(FlaskForm):
    email = EmailField(
        'Email',
        validators=[
            Email()
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ],
        description='Password'
    )


class RegistrationForm(LoginForm):
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords do not match'),
            Length(min=6, message='Password must be longer than 6 characters')
        ],
    )
