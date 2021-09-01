
from flask import Flask

from .blueprints.api.routes import api

from .telegram import telebot

from .config import API_KEY, db

from .models import message, user

from telegram.ext import Updater


def create_app(config):
    # Instance of flask app
    app = Flask(__name__)

    # Config of database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/sqlite.db'

    # Db init
    db.init_app(app)

    # create db tables
    with app.app_context():
        db.create_all()

    # Config of Blueprints
    app.register_blueprint(api)

    # Config of bot
    print("Bot started...")

    updater = Updater(token=API_KEY)
    dispatcher = updater.dispatcher

    # Bot Handlers
    dispatcher.add_handler(telebot.start_handler)
    dispatcher.add_handler(telebot.echo_handler)
    dispatcher.add_handler(telebot.caps_handler)
    dispatcher.add_handler(telebot.help_handler)
    dispatcher.add_handler(telebot.register_intro_handler)
    dispatcher.add_handler(telebot.register_handler)
    dispatcher.add_handler(telebot.unknown_handler)

    # Bot loop
    updater.start_polling()

    return app


# updater.stop()
