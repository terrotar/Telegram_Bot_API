from app.config import db

# Create getters
from sqlalchemy.ext.hybrid import hybrid_property


class Message(db.Model):
    __tablename__ = "mensagem"
    __id_message = db.Column("id_mensagem",
                             db.Integer,
                             primary_key=True)
    __text = db.Column("text",
                       db.String,
                       nullable=False)
    __username = db.Column("username",
                           db.String,
                           nullable=True)
    __first_name = db.Column("first_name",
                             db.String,
                             nullable=False)
    __last_name = db.Column("last_name",
                            db.String,
                            nullable=True)
    __cel_number = db.Column("cel_number",
                             db.String,
                             nullable=False)
    __id_user = db.Column("id_user",
                          db.BigInteger,
                          db.ForeignKey('usuario.id_user'))

    def __init__(self, text, username, first_name, last_name, cel_number):
        self.__text = text
        self.__username = self.__id_user.username
        self.__first_name = self.__id_user.first_name
        self.__last_name = self.__id_user.last_name
        self.__cel_number = self.__id_user.cel_number

    # GETTERS
    # id_message
    @hybrid_property
    def id_message(self):
        return self.__id_message

    # text
    @hybrid_property
    def text(self):
        return self.__text
