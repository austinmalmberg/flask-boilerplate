from werkzeug.security import generate_password_hash, check_password_hash

from app.database import db
from app.database.models import User


def get_user_by_id(id):
    return User.query.get(id)


def create_user(email, password):
    password_hash = generate_password_hash(password)

    user = User(email, password_hash)

    db.session.add(user)

    db.session.flush()
    db.session.commit()

    return user


def get_user_by_credentials(email, password):
    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password_hash, password):
        return user

    return None
