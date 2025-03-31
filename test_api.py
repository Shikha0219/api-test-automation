import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    """Test GET request to fetch posts."""
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert "title" in response.json()

def test_create_post():
    """Test POST request to create a new post."""
    data = {"title": "Test", "body": "This is a test post.", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=data)
    assert response.status_code == 201
    assert response.json()["title"] == data["title"]
