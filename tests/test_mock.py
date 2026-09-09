from unittest.mock import Mock

def test_mock_object():
    email_service = Mock() 

    email_service.send_email("shweta@gmail.com", "Hello") 

from unittest.mock import Mock

def test_mock_return_value():   
    payment_service = Mock() 
    payment_service.pay.return_value = "payment successful" 
    result = payment_service.pay(100)
    payment_service.pay.assert_called() 
    assert result == "payment successful" 