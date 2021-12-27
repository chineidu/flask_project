import json


def test_add_user(test_app, test_db):
    with test_app.test_client() as client:
        response = client.post(
            "/users",
            data=json.dumps({"username": "michael", "email": "michael@testdriven.io"}),
            content_type="application/json",
        )
        data = json.loads(response.data.decode("utf-8"))
        assert response.status_code == 201
        assert "michael@testdriven.io was added!" in data.get("message")
