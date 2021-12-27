from flask import Blueprint
from flask_restx import Api, Resource


ping_bp = Blueprint("Ping", __name__)
api = Api(ping_bp)


@api.route("/ping")
class Ping(Resource):
    def get(self):
        return {"status": "success", "message": "pong!"}
