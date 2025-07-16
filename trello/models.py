from email.policy import default

from . import db,login_manager
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(10), nullable = False)
    is_premium = db.Column(db.Boolean, default = False)
    is_public = db.Column(db.Boolean, default = True)
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
    postion = db.Column(db.Integer)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    cards = db.relationship('Card', backref='list', lazy=True)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_title = db.Column(db.String(100))
    status = db.Column(db.Boolean, default = False)
    description = db.Column(db.String)
    dueDate = db.Column(db.DateTime, nullable=False)
    list_id = db.Column(db.Integer , db.ForeignKey('list.id'), nullable = False)
    cardactivitys = db.relationship('CardActivity', backref='card', lazy=True)

class CheckList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    items = db.relationship('CheckListItem', backref='checklist', lazy=True)

class CheckListItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    position = db.Column(db.Integer, default=0)
    checklist_id = db.Column(db.Integer, db.ForeignKey('checklist.id'), nullable=False)

class CardActivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.Integer,  db.ForeignKey(Card.id))


class Attachment(db.Model):
    pass



