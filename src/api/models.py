from sqlalchemy.sql import func
from src import db


class Users(db.Model):
    __tablename__ = "users"

    # id username email active
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean(), nullable=False, default=True)
    created_date = db.Column(db.DateTime, nullable=False, default=func.now())

    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email
