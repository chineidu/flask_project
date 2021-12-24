import os
from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy


# instantiate the app
app = Flask(__name__)

api = Api(app)

db = SQLAlchemy()

# set config
app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)

db.init_app(app)


class Users(db.Model):
    __tablename__ = "users"

    # id username email active
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean(), nullable=False, default=True)

    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email


@api.route("/ping")
class Ping(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}
