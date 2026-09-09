import user_service

def test_get_username(monkeypatch):
    def fake_username():
        return "Shweta"
    
    monkeypatch.setattr(user_service, "get_username", fake_username)
    result = user_service.get_username()
    assert result == "Shweta" 