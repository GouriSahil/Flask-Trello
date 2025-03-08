from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trello.db'
app.config['SECRET_KEY'] = b'edcb482af610e1ef8a1165d565256b37'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from . import routes