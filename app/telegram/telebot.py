
from telegram.ext import CommandHandler, MessageHandler, Filters


# BOT COMMANDS

# Start
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""
             Bem-vindo ao WebDevTestBot =]\n
             Para receber mensagens é necessário
             realizar o cadastro /register\n
             Caso esteja em duvida /help
             """)


# Caps
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text_caps)


# Echo
def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text)


# Help
def help_user(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""
             Para interagir com o bot é muito fácil! Basta digitar os comandos ou clicar neles\n
             Cadastro:
             nome, sobrenome, celular\n
             Comandos:
             Cadastro /register
             Ajuda /help
             """)


# MUST BE LAST
# Unknown
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Desculpe mas não entendi. Digite /help caso precise de ajuda.")


# BOT HANDLERS


# COMMANDS

# Start
start_handler = CommandHandler('start', start)


# Caps
caps_handler = CommandHandler('caps', caps)


# Help
help_handler = CommandHandler('help', help_user)

# MESSAGES

# Echo
# & (~Filters.command)
# and is not a command text
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)


# MUST BE LAST
# Unknown
unknown_handler = MessageHandler(Filters.command, unknown)
