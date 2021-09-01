
from telegram.ext import CommandHandler, MessageHandler, Filters

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


# Register
def check_value(user_input):
    if (user_input):
        checker = user_input.split(" ")
        if (len(checker) == 3):
            try:
                isinstance(int(checker[2]), int) is True
            except Exception:
                return False
    return False


# Register_intro
def register_intro(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""
Você irá digitar seu primeiro nome, sobrenome e celular separados por espaços.
Exemplo:\n
Pedro Guedes 11953842552\n
/entendi
""")


# Register command /entendi
def register(update, context):
    user_input = update.message.text
    if (check_value(user_input) is True):
        user_input = user_input.split(" ")
        new_user = User(first_name=user_input[0],
                        last_name=user_input[1],
                        cel_number=user_input[2])
        db.session.add(new_user)
        db.commit()


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


# register_intro
register_intro_handler = CommandHandler('register', register_intro)


# Register
register_handler = CommandHandler('entendi', register)

# MESSAGES

# Echo
# & (~Filters.command)
# and is not a command text
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)


# MUST BE LAST
# Unknown
unknown_handler = MessageHandler(Filters.command, unknown)
