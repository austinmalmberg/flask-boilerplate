from datetime import datetime

from flask_login import UserMixin

from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creation_dt = db.Column(db.DateTime, default=datetime.utcnow())
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(), nullable=False)

    def __init__(self, email, password_hash):
        self.email = email
        self.password_hash = password_hash
