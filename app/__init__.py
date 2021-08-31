
from flask import Flask

from .blueprints.api.routes import api

from .telegram import telebot

from .config import API_KEY, db, bot

from telegram.ext import Updater


def create_app(config):
    # Instance of flask app
    app = Flask(__name__)

    # Config of database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/sqlite.db'
    db.init_app(app)
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

    # Bot loop
    updater.start_polling()

    return app


# updater.stop()
