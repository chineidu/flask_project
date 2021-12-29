import json
from src.status import status_code


def test_add_user(test_app, test_database):
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


def test_add_user_invalid_json(test_app, test_database):
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


def test_add_user_invalid_json_keys(test_app, test_database):
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


def test_add_user_duplicate_email(test_app, test_database):
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


def test_single_user(test_app, test_database, add_user):
    """This is used to test the route for retrieving a single user."""
    # Given
    user = add_user("jeffrey", "jeffrey@testdriven.io")
    with test_app.test_client() as client:

        # When
        response = client.get(f"/users/{user.id}")
        data = json.loads(response.data.decode("utf-8"))

        # Then
        assert response.status_code == status_code.OK_200
        assert "jeffrey" in data.get("username")
        assert "jeffrey@testdriven.io" in data.get("email")


def test_single_user_incorrect_id(test_app, test_database, add_user):
    # Given
    with test_app.test_client() as client:

        # When
        response = client.get(f"users/999")
        data = json.loads(response.data.decode("utf-8"))

        # Then
        assert response.status_code == status_code.NOT_FOUND_404
        assert "User 999 does not exist" in data.get("message")


# def test_all_users(test_app, test_database, add_user):
#     add_user("michael", "michael@mherman.org")
#     add_user("fletcher", "fletcher@notreal.com")
#     with test_app.test_client() as client:
#         response = client.get("/users")
#         data = json.loads(response.data.decode("utf-8"))
#         assert response.status_code == status_code.OK_200
#         assert len(data) == 2
#         assert "michael" in data[0].get("username")
#         assert "michael@mherman.org" in data[0].get("email")
#         assert "fletcher" in data[1].get("username")
#         assert "fletcher@notreal.com" in data[1].get("email")
