
from telegram.ext import CommandHandler, MessageHandler, Filters


# BOT COMMANDS

# Start
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Bem-vindo ao WebDevTestBot!")


# Echo
def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text)


# Caps
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text_caps)


# MUST BE LAST
# Unknown
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Desculpe mas não entendi.Digite /help caso precise de ajuda.")


# BOT HANDLERS

# Start
start_handler = CommandHandler('start', start)

# Echo
# & (~Filters.command)
# and is not a command text
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

# Caps
caps_handler = CommandHandler('caps', caps)

# MUST BE LAST
unknown_handler = MessageHandler(Filters.command, unknown)
