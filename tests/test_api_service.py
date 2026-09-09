from unittest.mock import patch
from api_service import get_user


@patch("api_service.requests.get")
def test_get_user(mock_get):
    mock_get.return_value.json.return_value = {
        "name": "Shweta",
        "role": "developer"
    }

    result = get_user()

    assert result == {
        "name": "Shweta",
        "role": "developer"
    } 

    mock_get.assert_called_once_with("https://example.com/user") 

from unittest.mock import patch
from api_service import get_user


@patch("api_service.requests.get")
def test_get_user(mock_get):

    mock_get.return_value.json.return_value = {
        "id": 1,
        "name": "Shweta",
        "role": "developer"
    }

    result = get_user()

    assert result["name"] == "Shweta"
    assert result["role"] == "developer"

    mock_get.assert_called_once_with(
        "https://example.com/user"
    ) 