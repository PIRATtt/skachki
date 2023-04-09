from flask.testing import FlaskClient
from app import app

print('Test code!')

def test_jockeys():
    with app.test_client() as client:
        response = client.get('/jockeys')
        assert response.status_code == 200

def test_index():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 201

def test_append():
    with app.test_client() as client:
        response = client.get('/append')
        assert response.status_code == 200

def test_battles():
    with app.test_client() as client:
        response = client.get('/battles')
        assert response.status_code == 200

def test_horses():
    with app.test_client() as client:
        response = client.get('/horses')
        assert response.status_code == 200
