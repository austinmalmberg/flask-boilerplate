
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user

from app.data_access.user import create_user, get_user_by_credentials
from app.forms.auth import RegistrationForm, LoginForm

bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        user = create_user(form.email.data, form.password.data)

        login_user(user)

        return redirect(url_for('index'))

    return render_template('auth.html', form=form, form_name='Register')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        user = get_user_by_credentials(form.email.data, form.password.data)

        if user is not None:
            login_user(user)
            return redirect(url_for('index'))

        flash('Invalid email or password')


    return render_template('auth.html', form=form, form_name='Login')


@bp.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('index'))
