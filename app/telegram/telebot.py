
from telegram import KeyboardButton, ReplyKeyboardMarkup

from telegram.ext import CommandHandler, MessageHandler, Filters

# Module created to make easier the database management
from .dbhelper import DBHelper

from loguru import logger

from datetime import date


# Instance of database's helper class
db = DBHelper()


# BOT COMMANDS

# Start
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"""
Oi {update.message.from_user.first_name} =]
Bem-vindo ao WebDevTestBot!\n
Para receber mensagens é necessário
realizar o cadastro /register\n
Caso esteja em duvida /help
             """)
    logger.success({"Telebot": {"status": "True", "data": [
                   "start_chat", {"user_id": f"{update.message.from_user.id}"}]}})


# Help
def help_user(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""
             Para interagir com o bot é muito fácil! Basta digitar os comandos ou clicar neles\n
             Cadastro:
             Compartilhar número de celular\n
             Comandos:
             Cadastro /register
             Ajuda /help
             """)
    logger.info({"Telebot": {"status": "True", "data": [
                "command_help", {"user_id": f"{update.message.from_user.id}"}]}})


# Register
def register(update, context):
    # Button to confirm share cel_number, deny or get help
    keyboard = [
        [KeyboardButton("Claro!", request_contact=True)],
        [KeyboardButton("/help")]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="""
Para continuar o cadastro é necessário compartilhar seu celular.\n
Caso tenha dúvidas, clique ou digite /help
                                  """,
                             reply_markup=reply_markup)
    logger.info({"Telebot": {"status": "True", "data": [
                "command_register", {"user_id": f"{update.message.from_user.id}"}]}})


# Contact Callback
def contact_callback(update, context):
    register = date.today()
    # datetime.date(byear, bmonth, bday)
    contact = update.effective_message.contact
    if (contact):
            db.add_user(contact.user_id, update.message.from_user.username, contact.first_name,
                        contact.last_name, contact.phone_number, register)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Parabéns!\nVocê acaba de se registrar no WebDevTestBot!")
            logger.success({"Telebot": {"status": "True", "data": [
                           "new_user", {"user_id": f"{contact.user_id}"}]}})


# MUST BE LAST
# Unknown
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Desculpe mas não entendi. Digite /help caso precise de ajuda.")
    logger.error({"Telebot": {"status": "null", "data": "unknown_command"}})


# BOT HANDLERS


# COMMANDS

# Start
start_handler = CommandHandler('start', start)


# Help
help_handler = CommandHandler('help', help_user)


# register
register_handler = CommandHandler('register', register)


# MESSAGES


# Contact
contact_handler = MessageHandler(Filters.contact, contact_callback)


# MUST BE LAST
# Unknown
unknown_handler = MessageHandler(Filters.command, unknown)
