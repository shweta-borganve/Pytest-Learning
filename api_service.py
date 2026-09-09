import requests

def get_user():
    response = requests.get("https://example.com/user")
    return response.json() 