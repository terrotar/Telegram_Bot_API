
import telegram

from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow


db = SQLAlchemy()


API_KEY = "1963801639:AAH4De3n2z9r_4AJjL5pI5b_f_qDMplbJ0w"

bot = telegram.Bot(token=API_KEY)

# This key should be private 
SECRET_KEY = '2\xa8\x1e\x98\x0f:\xce\x95[\xe1\x1fV\x1a\x8drj'


ma = Marshmallow()
