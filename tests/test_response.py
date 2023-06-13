import pytest
import requests

def test_server_response():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200 
    

