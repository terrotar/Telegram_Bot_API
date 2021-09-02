
from flask import Blueprint, jsonify, request

from ...models.user import User, user_schema, users_schema

from ...config import API_KEY

import requests


# Instance of Blueprint api with url_prefix
api = Blueprint('api', __name__, url_prefix="/api")


# Route to get all_users
@api.route("/all_users", methods=["GET"])
def get_users():
    if (request.method == "GET"):
        users = User.query.all()
        all_users = jsonify(users_schema.dump(users))
        return all_users


# Route to get certain user
@api.route("/user/get/<id_user>", methods=["GET"])
def get_user(id_user):
    if (request.method == "GET"):
        user = User.query.get(id_user)
        user = jsonify(user_schema.dump(user))
        return user


# Route to send a msg to a certain user
@api.route("/user/<id_user>/message/<message>", methods=["POST"])
def message_user(id_user, message):
    if (request.method == "POST"):
        send_text = f'https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={id_user}&text={message}'
        response = requests.post(send_text, API_KEY=API_KEY, id_user=id_user, message=message)
        return response.json()
