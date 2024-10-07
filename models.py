from flask_login import UserMixin
from database import get_db_connection

class User(UserMixin):
    def __init__(self, username, password, drive_link):
        self.id = username
        self.password = password
        self.drive_link = drive_link

    @staticmethod
    def get(username):
        conn = get_db_connection()
        user_row = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        if user_row:
            return User(user_row['username'], user_row['password'], user_row['drive_link'])
        return None
