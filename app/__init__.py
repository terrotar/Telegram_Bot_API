
from flask import Flask

from .blueprints.telegram.routes import telebot, sample_responses

from .config import API_KEY, db

import telegram

from telegram.ext import *


def create_app(config):
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/sqlite.db'

    db.init_app(app)

    with app.app_context():
        db.create_all()

    telegram.Bot(token=API_KEY)

    app.register_blueprint(telebot)

    main_bot()

    return app


# Setup of telegram bot start-up
def main_bot():

    print("Bot started...")

    updater = Updater(API_KEY)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


# Bot commands
def start_command(update, context):
    update.message.reply_text("Type something random to get started!")


def help_command(update, context):
    update.message.reply_text("If you need help you should as Google!")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")
