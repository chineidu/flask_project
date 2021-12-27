from src import create_app, db
from pytest import fixture


@fixture(scope="module")
def test_app():
    app = create_app()
    with app.app_context():
        yield app  # testing happens here


@fixture(scope="module")
def test_db():
    db.create_all()
    yield db  # testing happens here
    db.session.remove()
    db.drop_all()
