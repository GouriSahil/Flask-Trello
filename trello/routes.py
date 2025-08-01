from . import api , app
from trello.auth_resource import UserLogin,Userregistration , ProtectedResource
from flask import render_template



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


api.add_resource(Userregistration, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(ProtectedResource, '/secure')




