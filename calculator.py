def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b 

def greet(name):
    return f"Hello, {name}!" 

def calculate_total(prices):
    return sum(prices) 

def get_user_profile(user, role, active):
    return {
        "name" : "Shweta" ,
        "role" : "developer" ,
        "active" : True    
        } 

def find_item(items, target):
    if target in items:
        return target
    return None 

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b 