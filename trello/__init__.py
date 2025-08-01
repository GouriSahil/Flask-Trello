from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin , LoginManager
from flask_restful import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trello.db'
app.config['SECRET_KEY'] = b'edcb482af610e1ef8a1165d565256b37'
app.config["JWT_SECRET_KEY"] ='917fe44f2093a2f1bb680e8ba7cf458cf986dd4de560850742849c29c869'
db = SQLAlchemy(app)
api = Api(app )
jwt = JWTManager(app)
migrate = Migrate(app,db)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "Login"

from .models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from . import routes