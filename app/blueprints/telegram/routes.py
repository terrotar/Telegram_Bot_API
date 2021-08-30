
from flask import Blueprint


telebot = Blueprint('telebot', __name__)


def sample_responses(input_text):

    user_message = str(input_text).lower()

    if user_message in ("hello"):
        return "Hey! How's it going?"

    if user_message in ("who are you", "who are you?"):
        return "I am bot!"

    return "I don't understand you."
