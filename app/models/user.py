
from app.config import db


class User(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
