
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
@api.route("/user/<user_id>/message/<message>", methods=["GET", "POST"])
def message_user(user_id, message):
    # Bot_key
    bot = API_KEY
    # URL
    send_text = f'https://api.telegram.org/bot{bot}/sendMessage'
    # Parameters
    params = {"chat_id": str(user_id), "text": str(message)}
    # Response
    response = requests.post(send_text, params)
    return response.text
