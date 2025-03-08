from flask import Flask,render_template, url_for
from . import app


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/')
def home():
    return render_template('home.html')