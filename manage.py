from flask.cli import FlaskGroup
from src import app


cli = FlaskGroup(app)  # used to extend the CLI with commands related to the Flask app.

if __name__ == "__main__":
    cli()
