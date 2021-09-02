
from flask import Flask

from .blueprints.api.routes import api
from .blueprints.telegram_user.routes import telegram_user

from .telegram import telebot

from .config import API_KEY, db, SECRET_KEY

from .models import message, user

from telegram.ext import Updater


def create_app(config):
    # Instance of flask app
    app = Flask(__name__)

    # Instance app.config == 'config.py'
    app.config.from_pyfile('config.py')

    # Config of database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/sqlite.db'
    app.config['SECRET_KEY'] = SECRET_KEY

    # Db init
    db.init_app(app)

    # create db tables
    app.app_context().push()
    db.create_all()

    # Config of Blueprints
    app.register_blueprint(api)
    app.register_blueprint(telegram_user)

    # Config of bot
    print("Bot started...")

    updater = Updater(token=API_KEY)
    dispatcher = updater.dispatcher

    # Bot Handlers
    dispatcher.add_handler(telebot.start_handler)
    dispatcher.add_handler(telebot.help_handler)
    dispatcher.add_handler(telebot.register_handler)
    # dispatcher.add_handler(telebot.buttons_handler)
    dispatcher.add_handler(telebot.contact_handler)
    dispatcher.add_handler(telebot.unknown_handler)

    # Bot loop
    updater.start_polling()

    return app
