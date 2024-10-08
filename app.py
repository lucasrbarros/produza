# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from auth import authenticate_user
from models import User
from database import initialize_db

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

# Inicializar Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

initialize_db()

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = authenticate_user(username, password)
        if user:
            login_user(user)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login inválido. Verifique seu usuário e senha.', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', drive_link=current_user.drive_link)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu com sucesso.', 'success')
    return redirect(url_for('login'))


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        drive_link = request.form['drive_link']
        
        success = User.create(username, password, drive_link)
        if success:
            flash(f'Usuário {username} adicionado com sucesso!', 'success')
            return redirect(url_for('admin'))
        else:
            flash(f'Erro: O usuário {username} já existe.', 'danger')
    
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
