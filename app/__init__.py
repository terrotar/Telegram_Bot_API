
from flask import Flask

from .blueprints.telegram.routes import telegram


def create_app(config):
    app = Flask(__name__)

    app.register_blueprint(telegram)

    return app
