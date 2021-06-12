import os

from flask import Flask

from app import database, routes
from app.helpers import user_manager


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL'],
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # flask_login initialization
    user_manager.init_app(app)

    # database initialization
    database.init_app(app)

    routes.register_blueprints(app)
    app.add_url_rule('/', 'index')

    return app