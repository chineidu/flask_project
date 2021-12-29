from src import create_app, db
from src.api.models import Users
from pytest import fixture


@fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object("src.config.TestingConfig")
    with app.app_context():
        yield app  # testing happens here


@fixture(scope="module")
def test_database():
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()


@fixture(scope="function")
def add_user():
    """This is used to add a new user to the database. It takes a
    function as an input."""

    def _add_user(username: str, email: str) -> Users:
        user = Users(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    return _add_user
