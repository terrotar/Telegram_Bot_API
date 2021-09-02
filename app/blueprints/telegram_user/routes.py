
from flask import Blueprint

from app.config import db

from app.models.user import User


telegram_user = Blueprint('telegram_user', __name__, url_prefix="/user")
