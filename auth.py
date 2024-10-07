from flask_login import LoginManager
from models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

def authenticate_user(username, password):
    user = User.get(username)
    if user and user.password == password:
        return user
    return None
