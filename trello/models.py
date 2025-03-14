from . import db,login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(10), nullable = False)
    boards = db.relationship('Board', backref='user', lazy = True)

    def __repr__(self):
        return f"{self.username}, {self.email}"

class Board(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    board_title = db.Column(db.String(100))
    user_id = db.Column(db.Integer , db.ForeignKey('user.id'), nullable = False)
    lists = db.relationship('List', backref='board', lazy=True)

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_title = db.Column(db.String(80))
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    cards = db.relationship('Card', backref='list', lazy=True)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_title = db.Column(db.String(100))
    list_id = db.Column(db.Integer , db.ForeignKey('list.id'), nullable = False)