import os


def test_development_config(test_app):
    test_app.config.from_object("src.config.DevelopmentConfig")
    assert test_app.config.get("SECRET_KEY") == "my_precious"
    assert not test_app.config.get("TESTING")
    assert test_app.config.get("SQLALCHEMY_DATABASE_URI") == os.getenv("DATABASE_URL") 


def test_testing_config(test_app):
    test_app.config.from_object("src.config.TestingConfig")
    assert test_app.config.get("SECRET_KEY") == "my_precious"
    assert test_app.config.get("TESTING")
    assert not test_app.config.get("PRESERVE_CONTEXT_ON_EXCEPTION")
    assert test_app.config.get("SQLALCHEMY_DATABASE_URI") == os.getenv("DATABASE_TEST_URL")


def test_production_config(test_app):
    test_app.config.from_object("src.config.ProductionConfig")
    assert test_app.config.get("SECRET_KEY") == "my_precious"
    assert not test_app.config.get("TESTING")
    assert test_app.config.get("SQLALCHEMY_DATABASE_URI") == os.getenv("DATABASE_URL")     