from app.config import db

# Create getters
from sqlalchemy.ext.hybrid import hybrid_property


class Message(db.Model):
    __tablename__ = "mensagem"
    __id_message = db.Column("id_mensagem", db.Integer, primary_key=True)
    __text = db.Column("text", db.String, nullable=False)
    __first_name = db.Column("first_name", db.String, db.ForeignKey('usuario.first_name'))
    __last_name = db.Column("last_name", db.String, db.ForeignKey('usuario.last_name'))
    __cel_number = db.Column("cel_number", db.String, db.ForeignKey('usuario.cel_number'))
    __id_user = db.Column("id_user", db.BigInteger, db.ForeignKey('usuario.id_user'))

    def __init__(self, text):
        self.__text = text

    # GETTERS
    # id_message
    @hybrid_property
    def id_message(self):
        return self.__id_message

    # text
    @hybrid_property
    def text(self):
        return self.__text
