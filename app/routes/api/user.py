
from flask import Blueprint, jsonify
from flask_login import login_required, current_user

bp = Blueprint('users', __name__, url_prefix='/user')


@bp.route('/')
@login_required
def current_user():
    return jsonify(current_user)