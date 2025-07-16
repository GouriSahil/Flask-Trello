from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin , LoginManager
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trello.db'
app.config['SECRET_KEY'] = b'edcb482af610e1ef8a1165d565256b37'
db = SQLAlchemy(app)
Migrate(app,db)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "Login"
from .models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from . import routes