from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {'name':'Vansh', 'email':'vansh@gmail.com'}

def test_current_user():
    response = client.get("/current-user")

    assert response.status_code == 200
    assert response.json() == {'id':'yetr643r6346rt46r64r4rr4', 'email':'vansh@gmail.com', 'age':23}