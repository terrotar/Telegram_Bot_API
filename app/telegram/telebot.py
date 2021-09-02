
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update

from telegram.ext import CallbackQueryHandler, CallbackContext, CommandHandler, MessageHandler, Filters

from app.config import db

from app.models.user import User


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


# Contact Callback
def contact_callback(update, context):
    contact = update.effective_message.contact
    if (contact):
        phone = contact.phone_number
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"cel: {phone}\ncontact: {contact}")


# MUST BE LAST
# Unknown
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Desculpe mas não entendi. Digite /help caso precise de ajuda.")


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
