import json


def test_ping(test_app):
    # Given
    with test_app.test_client() as client:
        
        # When
        response = client.get("/ping")
        data = json.loads(response.data.decode("utf-8"))
        
        # Then
        assert response.status_code == 200
        assert "success" in data.get("status")
        assert "pong!" in data.get("message")
