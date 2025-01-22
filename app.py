from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session

from datetime import datetime, timedelta

from database.db import get_connection

"""
Initializing Application

"""

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)


"""
App Routing 

The following routes are defined:
- /         :   This is the default non-logged in user. From here, 
                the user can be redirected to the login page.
                
                Note that the APP can only be accessed by EMPLOYEES
                of the company, specifically managers and cashiers.
                Thus, there are pre-set accounts for employees that handle
                the sales of the company.

- /login    :   This is the login page. Pre-defined users only. No registration.
                Only ADMINS have access to adding new users to the system. 

"""

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

        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        if user:
            session['user'] = user
            return redirect(url_for('main'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html')

if __name__ == "__main__":
  app.run()

