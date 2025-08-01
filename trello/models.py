from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from . import db

CardUser = db.Table(
    'card_user',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', name='fk_card_user_user_id'), primary_key=True),
    db.Column('card_id', db.Integer, db.ForeignKey('card.id', name='fk_card_user_card_id'), primary_key=True)
)

class BoardMember(db.Model):
    __tablename__ = 'user_board'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_user_board_user_id'), primary_key=True)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id', name='fk_user_board_board_id'), primary_key=True)
    role = db.Column(db.String(20))  # 'admin' or 'member'
    user = db.relationship('User', back_populates='user_boards')
    board = db.relationship('Board', back_populates='user_boards')
    
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_premium = db.Column(db.Boolean, default=False)
    user_boards = db.relationship('BoardMember', back_populates='user')
    assigned_cards = db.relationship('Card', secondary=CardUser, back_populates='assignees')
    boards = db.relationship('Board', secondary='user_board', back_populates='assignees', viewonly=True)

    def __repr__(self):
        return f"{self.username}, {self.email}"

class Board(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.Integer, primary_key=True)
    board_title = db.Column(db.String(100))
    lists = db.relationship('List', backref='board', lazy=True)
    user_boards = db.relationship('BoardMember', back_populates='board')
    assignees = db.relationship('User', secondary='user_board', back_populates='boards', viewonly=True)

class List(db.Model):
    __tablename__ = 'list'
    id = db.Column(db.Integer, primary_key=True)
    list_title = db.Column(db.String(80))
    position = db.Column(db.Integer)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id', name='fk_list_board_id'), nullable=False)
    cards = db.relationship('Card', backref='list', lazy=True)

class Card(db.Model):
    __tablename__ = 'card'
    id = db.Column(db.Integer, primary_key=True)
    card_title = db.Column(db.String(100))
    status = db.Column(db.Boolean, default=False)
    description = db.Column(db.String)
    due_date = db.Column(db.DateTime, nullable=False)
    position = db.Column(db.Integer, default=0)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id', name='fk_card_list_id'), nullable=False)
    card_activities = db.relationship('CardActivity', back_populates='card', lazy=True)
    assignees = db.relationship('User', secondary=CardUser, back_populates='assigned_cards')

class CardActivity(db.Model):
    __tablename__ = 'cardactivity'
    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id', name='fk_card_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_card_id'))
    activity_type = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    details = db.Column(db.Text)
    card = db.relationship('Card', back_populates='card_activities')
    user = db.relationship('User')

class CheckList(db.Model):
    __tablename__ = 'checklist'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    items = db.relationship('CheckListItem', backref='checklist', lazy=True)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id', name='fk_card_id'), nullable=False)
    card = db.relationship('Card', backref='checklists')

class CheckListItem(db.Model):
    __tablename__ = 'checklistitem'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    position = db.Column(db.Integer, default=0)
    checklist_id = db.Column(db.Integer, db.ForeignKey('checklist.id', name='fk_checklist_id'), nullable=False)


class Attachment(db.Model):
    __tablename__ = 'attachment'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    url = db.Column(db.String(255))
    card_id = db.Column(db.Integer, db.ForeignKey('card.id', name='fk_card_id'), nullable=False)
    card = db.relationship('Card', backref='attachments')

