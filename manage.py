import sys
from flask.cli import FlaskGroup
from src import create_app, db
from src.api.models import Users


app = create_app()
cli = FlaskGroup(
    create_app=create_app
)  # used to extend the CLI with commands related to the Flask app.


@cli.command("recreate_db")
def recreate_db():
    """This is used to create a fresh database instance."""
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("populate_db")
def populate_db():
    """This is used to populate the database."""
    db.drop_all()
    db.create_all()

    user_1 = Users(username="Neidu", email="neidu@email.com")
    user_2 = Users(username="Stella", email="stella@email.com")
    db.session.add(user_1)
    db.session.add(user_2)
    db.session.commit()


if __name__ == "__main__":
    cli()
