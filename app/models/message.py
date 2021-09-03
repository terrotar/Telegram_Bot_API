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
                             nullable=True)
    __last_name = db.Column("last_name",
                            db.String,
                            nullable=True)
    __cel_number = db.Column("cel_number",
                             db.String,
                             nullable=True)
    id_user = db.Column(db.BigInteger,
                        db.ForeignKey('usuario.id_user'))

    # GETTERS
    # id_message
    @hybrid_property
    def id_message(self):
        return self.__id_message

    # text
    @hybrid_property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text

    # username
    @hybrid_property
    def username(self):
        return self.username

    @username.setter
    def username(self, username):
        self.__username = username

    # first_name
    @hybrid_property
    def first_name(self):
        return self.first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    # last_name
    @hybrid_property
    def last_name(self):
        return self.last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    # cel_number
    @hybrid_property
    def cel_number(self):
        return self.cel_number

    @cel_number.setter
    def cel_number(self, cel_number):
        self.__cel_number = cel_number
