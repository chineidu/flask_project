from flask import Blueprint
from flask_restx import Resource, Api, reqparse
from src import db
from .models import Users


users_bp = Blueprint("Users", __name__)
api = Api(users_bp)

parser = reqparse.RequestParser()
parser.add_argument("username", required=True, type=str, help="Enter the username ")
parser.add_argument("email", required=True, type=str, help="Enter the email ")


@api.route("/users")
class UsersList(Resource):
    def post(self):
        data = parser.parse_args()
        username = data.get("username")
        email = data.get("email")

        db.session.add(Users(username=username, email=email))
        db.session.commit()

        response_object = {"message": f"{email} was added!"}
        return response_object, 201
