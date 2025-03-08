from flask_bcrypt import Bcrypt
from trello import app,db
from trello.models import User

bcrypt = Bcrypt(app)

with app.app_context():
    db.create_all()

    hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
    user1 = User(username='Gouri Sahil', password=hashed_password)
    user2 = User(username='Asrar',  password=hashed_password)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    print("Database created and initial data added.")