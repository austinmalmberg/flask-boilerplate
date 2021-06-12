
from flask_login import LoginManager

from app.data_access.user import get_user_by_id

login = LoginManager()


def init_app(app):
    login.init_app(app)


@login.user_loader
def load_user(id):
    return get_user_by_id(id)
