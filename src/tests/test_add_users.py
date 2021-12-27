import json
from src.status import status_code


def test_add_user(test_app, test_db):
    """This is used to test the addition of a new user."""
    # Given
    with test_app.test_client() as client:
        
        # When
        response = client.post(
            "/users",
            data=json.dumps({"username": "michael", "email": "michael@testdriven.io"}),
            content_type="application/json",
        )
        data = json.loads(response.data.decode("utf-8"))
        
        # Then
        assert response.status_code == status_code.CREATED_201
        assert "michael@testdriven.io was added!" in data.get("message")


def test_add_user_invalid_json(test_app, test_db):
    """This is used to test the addition of a user with an empty payload."""
    # Given
    with test_app.test_client() as client:

        # When
        response = client.post(
            "/users", data=json.dumps({}), content_type="application/json"
        )
        data = json.loads(response.data.decode("utf-8"))
        
        # Then
        assert response.status_code == status_code.BAD_REQUEST_400
        assert "Input payload validation failed" in data.get("message")


def test_add_user_invalid_json_keys(test_app, test_db):
    """This is used to test the addition of a user with an invalid/incomplete keys"""
    # Given
    with test_app.test_client() as client:

        # When
        response = client.post(
            "/users",
            data=json.dumps({"email": "john@testdriven.io"}),
            content_type="application/json",
        )
        data = json.loads(response.data.decode("utf-8"))

        # Then
        assert response.status_code == status_code.BAD_REQUEST_400
        assert "Input payload validation failed" in data.get("message")


def test_add_user_duplicate_email(test_app, test_db):
    """This is used to test the addition of a user with an duplicate emails"""
    # Given
    with test_app.test_client() as client:
        # When
        response = client.post(
            "/users",
            data=json.dumps({"username": "michael", "email": "michael@testdriven.io"}),
            content_type="application/json",
        )
        data = json.loads(response.data.decode("utf-8"))
        # Then
        assert response.status_code == status_code.BAD_REQUEST_400
        assert "Sorry. That email already exists." in data.get("message")
