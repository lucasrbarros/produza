# auth.py

from models import User

def authenticate_user(username, password):
    user = User.get(username)
    if user and user.password == password:
        return user
    return None
