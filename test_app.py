from app import app

def test_greet():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Yo! Whats up?'