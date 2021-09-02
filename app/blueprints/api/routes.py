
from flask import Blueprint, jsonify

from ...models.user import User, user_schema, users_schema


api = Blueprint('api', __name__, url_prefix="/api")


@api.route("/all_users", methods=["GET"])
def get_users():
    users = User.query.all()
    all_users = jsonify(users_schema.dump(users))
    return all_users


@api.route("/user/<id_user>", methods=["GET"])
def get_user(id_user):
    user = User.query.get(id_user)
    user = jsonify(user_schema.dump(user))
    return user
