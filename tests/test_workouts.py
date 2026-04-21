def test_protected_requires_auth(client):
    response = client.get("/workouts/")
    assert response.status_code == 401