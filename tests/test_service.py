from unittest.mock import Mock
from service import send_request

def test_send_request(monkeypatch):
    api_service = Mock() 
    monkeypatch.setenv("API_KEY", "test123")
    api_service.send.return_value = "Success"
    result = send_request(api_service)
    assert result == "Success"
    api_service.send.assert_called_once_with("test123") 