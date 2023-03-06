
import telegram

from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow


db = SQLAlchemy()


API_KEY = ""

bot = telegram.Bot(token=API_KEY)

# This key should be private 
SECRET_KEY = ''


ma = Marshmallow()
