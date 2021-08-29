
from flask import Flask

from .blueprints.telegram.routes import telegram

from .config import bot, bot_token, bot_user_name, TOKEN


def create_app(config):
    app = Flask(__name__)

    app.register_blueprint(telegram)

    return app
