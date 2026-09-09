from config import get_api_key 

def test_get_api_key(monkeypatch):
    monkeypatch.setenv("API_KEY", "test123")
    result = get_api_key()
    assert result == "test123" 