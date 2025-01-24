from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
from flask_bcrypt import Bcrypt

from datetime import datetime, timedelta

from database.db import get_connection

"""
Initializing Application

This is the basic Flask startup method for the web-app to run.
"""
app = Flask(__name__)
bycrypt = Bcrypt(app)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)



"""
APP ROUTING

The following routes are defined:
- /         :   This is the default non-logged in user. From here, 
                the user can be redirected to the login page.
                
                Note that the APP can only be accessed by EMPLOYEES
                of the company, specifically managers and cashiers.
                Thus, there are pre-set accounts for employees that handle
                the sales of the company.

- /login    :   This is the login page. Pre-defined users only. No registration.
                Only ADMINS have access to adding new users to the system. 

- /register :   This is the registration page. Only ADMINS have access to this page.
                This is where new employees can be added to the system.

- /main     :   This is the landing page for employees. This is where the main directory will be displayed
                In main, the employee is able to go through different features of the application.
                It could be sales, viewing sales history, check product prices, and other basic applications of a POS-System

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


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
        conn.commit()

        return redirect(url_for('login'))

    return render_template('register.html')
