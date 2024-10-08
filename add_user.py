# add_user.py

from models import User
from database import get_db_connection, initialize_db
import sys

def add_user(username, password, drive_link):
    initialize_db()  # Certifica-se de que o banco de dados está inicializado
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO users (username, password, drive_link) VALUES (?, ?, ?)',
                     (username, password, drive_link))
        conn.commit()
        print(f"Usuário '{username}' adicionado com sucesso!")
    except sqlite3.IntegrityError:
        print(f"Erro: O usuário '{username}' já existe.")
    finally:
        conn.close()

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Uso: python add_user.py <username> <password> <drive_link>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        drive_link = sys.argv[3]
        add_user(username, password, drive_link)
