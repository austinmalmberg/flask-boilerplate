
from flask_wtf import FlaskForm


class AppForm(FlaskForm):
    name = 'AppForm'
    button_text = ''
    action = ''
