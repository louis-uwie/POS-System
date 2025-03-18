from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
from flask_bcrypt import Bcrypt

from datetime import datetime, timedelta
from database.db import get_connection  # Ensure this function is correctly implemented

# Initialize Flask App
app = Flask(__name__)
bcrypt = Bcrypt(app)  # Fixed typo

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user and bcrypt.check_password_hash(user[2], password):  # Assuming password is the 3rd column
            session['user'] = user
            conn.close()
            return redirect(url_for('main'))
        else:
            conn.close()
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        # Hash the password before storing
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (username, hashed_password, role))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)  # Keep this at the bottom
