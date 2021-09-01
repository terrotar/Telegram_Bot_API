
from app.config import db

# Create getters
from sqlalchemy.ext.hybrid import hybrid_property


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

    # GETTERS
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
