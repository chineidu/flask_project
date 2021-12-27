import os
from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(script_info=None):
    """This uses the factory pattern to create a Flask app."""
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    db.init_app(app)

    # register the blueprints
    _register_blueprint(app)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app


def _register_blueprint(app):
    from src.api.ping import ping_bp
    from src.api.users import users_bp

    app.register_blueprint(ping_bp)
    app.register_blueprint(users_bp)
