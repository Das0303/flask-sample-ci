import pytest
from app import app

@pytest.fixture
def client():
    # Set up the Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Test the root route ('/') returns the expected content and status code."""
    # Make a GET request to the root URL
    response = client.get('/')
    
    # Check if the status code is 200 OK
    assert response.status_code == 200
    
    # Check if the response data contains the expected text
    assert b'Hello, World!' in response.data
