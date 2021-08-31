
from telegram.ext import CommandHandler


# Bot commands

# Start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot!")


# Bot Handlers

# Start Handler
start_handler = CommandHandler('start', start)
