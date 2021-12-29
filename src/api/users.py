from flask import Blueprint, current_app
from flask_restx import Resource, Api, reqparse, fields
from src import db
from src.api.models import Users
from src.status import status_code


users_bp = Blueprint("Users", __name__)
api = Api(users_bp)

users_model = api.model(
    "User",
    {
        "id": fields.Integer(readOnly=True),
        "username": fields.String(required=True),
        "email": fields.String(required=True),
        "created_date": fields.DateTime(readOnly=True),
    },
)

parser = reqparse.RequestParser()
parser.add_argument("username", type=str, help="Enter the username ")
parser.add_argument("email", type=str, help="Enter the email ")


@api.route("/users/<int:user_id>")
class Users_(Resource):
    @api.marshal_with(users_model)
    def get(self, user_id: int):
        user = Users.query.filter_by(id=user_id).first()
        if not user:
            current_app.logger.debug("USER RETRIEVAL FAILED!")
            return api.abort(404, f"User {user_id} does not exist")

        # else
        current_app.logger.info("USER SUCCESSFULLY RETRIEVED!")
        return user, status_code.OK_200


@api.route("/users")
class UsersList(Resource):
    @api.marshal_with(users_model, as_list=True)
    def get(self):
        user = Users.query.all()
        current_app.logger.info("ALL USERS SUCCESSFULLY RETRIEVED!")
        return user, status_code.OK_200

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
