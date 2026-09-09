import os

def get_api_key():
    return os.environ.get("API_KEY") 

def send_request(api_service):
    api_key = get_api_key()
    return api_service.send(api_key) 