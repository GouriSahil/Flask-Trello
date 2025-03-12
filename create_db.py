from flask_bcrypt import Bcrypt
from trello import app,db
from trello.models import User, Card , Board , List

bcrypt = Bcrypt(app)


with app.app_context():
    db.create_all()
    user = User.query.all()
    print(user)