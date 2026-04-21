
def test_create_user_success(client):
    response = client.post("/users/", json={
        "username": "test",
        "email": "test@test.com",
        "password": "test"
    })

    data = response.json()

    assert response.status_code == 200
    assert data["username"] == "test"
    assert "id" in data


def test_login_user_success(client):
    client.post("/users/", json={
        "username": "test",
        "email": "test@test.com",
        "password": "test"
    })

    response = client.post("/users/login", data={
        "username": "test",
        "password": "test"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_user_fail(client):

    response = client.post("/users/login", data={
        "username": "nope",
        "password": "nah"
    })

    assert response.status_code == 401


def test_duplicate_user_fails(client):
    client.post("/users/", json={
        "username": "dupe",
        "email": "dupe@test.com",
        "password": "dupe"
    })

    response = client.post("/users/", json={
        "username": "dupe",
        "email": "dupe@test.com",
        "password": "dupe"
    })

    assert response.status_code == 400

