
from flask import Blueprint, jsonify, request

from ...models.user import User, user_schema, users_schema

from ...models.message import Message

from ...config import API_KEY, db

import requests

from loguru import logger


# Instance of Blueprint api with url_prefix
api = Blueprint('api', __name__, url_prefix="/api")


# Route to get all_users
@api.route("/all_users", methods=["GET"])
def get_users():
    if (request.method == "GET"):
        users = User.query.all()
        all_users = jsonify(users_schema.dump(users))
        logger.success({"Request": {"status": "True", "data": "all_users"}})
        return all_users


# Route to get certain user
@api.route("/user/get/<id_user>", methods=["GET"])
def get_user(id_user):
    if (request.method == "GET"):
        user = User.query.get(id_user)
        user = jsonify(user_schema.dump(user))
        logger.success({"Request": {"status": "True", "data": ["get_user", {"id_user": f"{id_user}"}]}})
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
    # new_message
    new_message = Message()

    # Set user's message atributes
    user = User.query.get(user_id)

    new_message.text = message
    new_message.first_name = user.first_name
    new_message.cel_number = user.cel_number
    new_message.id_user = user.id_user

    if (user.last_name):
        new_message.last_name = user.last_name
    if (user.username):
        new_message.username = user.username
    # Instance new_message
    db.session.add(new_message)
    db.session.commit()
    logger.success({"Request": {"status": "True", "data": ["message_user", {"user_id": f"{user.id_user}"}]}})
    return response.text
