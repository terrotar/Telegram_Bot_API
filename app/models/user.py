
from app.config import db, ma

from .message import Message


# Create getters
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model):
    __tablename__ = "usuario"
    __id_user = db.Column("id_user",
                          db.BigInteger,
                          primary_key=True)
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
                             unique=True,
                             nullable=False)
    __join_date = db.Column("join_date",
                       db.Date,
                       unique=False,
                       nullable=False)
    __messages = db.relationship("Message", backref="messages")

    def __init__(self, id_user, username, first_name, last_name, cel_number, join_date):
        self.__id_user = id_user
        self.__username = username
        self.__first_name = first_name
        self.__last_name = last_name
        self.__cel_number = cel_number
        self.__join_date = join_date

    # GETTERS
    # id_user
    @hybrid_property
    def id_user(self):
        return self.__id_user

    # username
    @hybrid_property
    def username(self):
        return self.__username

    # first_name
    @hybrid_property
    def first_name(self):
        return self.__first_name

    # last_name
    @hybrid_property
    def last_name(self):
        return self.__last_name

    # cel_number
    @hybrid_property
    def cel_number(self):
        return self.__cel_number

    def send_message(self, text):
        new_message = Message(text=text)
        db.session.add(new_message)
        db.commit()
        return new_message


# Marshmallow Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ("id_user", "username", "first_name",
                  "last_name", "cel_number", "join_date")


# Loads in JSON one or many users
user_schema = UserSchema()
users_schema = UserSchema(many=True)
