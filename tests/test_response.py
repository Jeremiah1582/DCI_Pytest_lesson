import pytest
import requests

# test 1
# this test tests the status_code of the internet server get request 
def test_server_response():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200 
    
# test 2 
# 1. this test uses the @pytest.mark.skip() method to skip the test during testing
# 2. this code checks the length of the internet servers response
@pytest.mark.skip(reason="Reason for skipping the test") #this line allows you to skip the following test
def test_length_of_response():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert len(response.json()) != 0 
    

