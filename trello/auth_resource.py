from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token , jwt_required , get_jwt_identity
from trello.models import User
from trello import db
from . import bcrypt
class Userregistration(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username and not password:
            return {"message" : "username or password missing"}
        if User.query.filter_by(email=email).first():
            return {"message" : "Email already registered"},400
        
        hassed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username , email=email , password = hassed_password)
        db.session.add(user)
        db.session.commit()

        return {"message" : "User registerd sucessfully"}

class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        return {"message": f"Hello {current_user}, welcome to Trello!"}

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email = email).first()

        if user and bcrypt.check_password_hash(user.password , password):
            access_token = create_access_token(identity=str(user.id))
            return{"access token" : access_token},200
        return{"message": "Invalid credentials"}


        