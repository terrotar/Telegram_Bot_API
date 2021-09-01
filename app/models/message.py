from app.config import db

# Create getters
from sqlalchemy.ext.hybrid import hybrid_property


class Message(db.Model):
    __tablename__ = "mensagem"
    id = db.Column("id_mensagem", db.Integer, primary_key=True)
    __text = db.Column("text", db.String, nullable=False)
    __first_name = db.Column("first_name", db.String, db.ForeignKey('usuario.first_name'))
    __cel_number = db.Column("cel_number", db.BigInteger, db.ForeignKey('usuario.cel_number'))
    __user_id = db.Column("user_id", db.Integer, db.ForeignKey('usuario.id_user'))

    def __init__(self, text, first_name, cel_number, user_id):
        self.__text = text
        self.__first_name = first_name
        self.__cel_number = cel_number
        self.__user_id = user_id

    # GETTERS
    # text
    @hybrid_property
    def text(self):
        return self.__text

    # first_name
    @hybrid_property
    def first_name(self):
        return self.first_name

    # cel_number
    @hybrid_property
    def cel_number(self):
        return self.__cel_number

    # user_id
    @hybrid_property
    def user_id(self):
        return self.__user_id
