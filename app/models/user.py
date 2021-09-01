
from app.config import db


class User(db.Model):
    __tablename__ = "usuario"
    id = db.Column("id_user", db.Integer, primary_key=True)
    __first_name = db.Column("first_name", db.String, nullable=False)
    __last_name = db.Column("last_name", db.String, nullable=False)
    __cel_number = db.Column("cel_number", db.String, unique=True, nullable=False)

    def __init__(self, first_name, last_name, cel_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__cel_number = cel_number
