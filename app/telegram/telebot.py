
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


# Register_intro
def register(update: Update, context: CallbackContext) -> None:
    # Button to confirm share cel_number, deny or get help
    keyboard = [
        [
            KeyboardButton("Claro!", request_contact=True),
            KeyboardButton("Ahh... acho que não", callback_data="Que pena =["),
        ],
        [KeyboardButton("/help")],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="""
Para continuar o cadastro é necessário informar seu celular.\n
Caso tenha dúvidas, clique ou digite /help
                                  """,
                             reply_markup=reply_markup)


# Button Callback
def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text=f"Selected option: {query.message}")


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


# Button Callback
buttons_handler = CallbackQueryHandler(button)


# MUST BE LAST
# Unknown
unknown_handler = MessageHandler(Filters.command, unknown)
