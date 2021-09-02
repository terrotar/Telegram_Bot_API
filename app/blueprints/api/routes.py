
from flask import Blueprint, jsonify

from ...models.user import User, user_schema, users_schema


api = Blueprint('api', __name__, url_prefix="/api")


@api.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    all_users = jsonify(users_schema.dump(users))
    return all_users
