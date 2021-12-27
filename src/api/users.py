from flask import Blueprint, current_app
from flask_restx import Resource, Api, reqparse, fields
from src import db
from .models import Users
from src.status import status_code


users_bp = Blueprint("Users", __name__)
api = Api(users_bp)

users_model = api.model(
    "User",
    {
        "id": fields.Integer(readOnly=True),
        "username": fields.String(required=True),
        "email": fields.String(required=True),
        "created_at": fields.DateTime,
    },
)

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, help="Enter the username ")
parser.add_argument("email", type=str, help="Enter the email ")


@api.route("/users")
class UsersList(Resource):
    @api.expect(users_model, validate=True)
    def post(self):
        data = parser.parse_args()
        username = data.get("username")
        email = data.get("email")

        user = Users.query.filter_by(email=email).first()
        if user:
            current_app.logger.debug("USER CREATION FAILED!")
            response_object = {"message": "Sorry. That email already exists."}
            return response_object, status_code.BAD_REQUEST_400

        current_app.logger.info("USER SUCESSFULLY ADDED!")
        db.session.add(Users(username=username, email=email))
        db.session.commit()

        response_object = {"message": f"{email} was added!"}
        return response_object, status_code.CREATED_201
