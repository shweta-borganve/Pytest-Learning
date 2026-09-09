from unittest.mock import Mock
from database_service import get_user

def test_get_user():
    db = Mock()

    db.get_user.return_value = {'id' : 1, 'name': 'Shweta'}
    result = get_user(db) 
    assert result["name"] == "Shweta" 
    db.get_user.assert_called_once_with(1) 