import pytest

@pytest.fixture
def user():
    return {
        "name": "Shweta",
        "role": "developer",
        "active": True 
    } 

@pytest.fixture
def test_message():
    print("\n Setup: creating test message") 

    message = "Hello, pytest!"
    yield message

    print("\n Teardown: cleaning up after test") 