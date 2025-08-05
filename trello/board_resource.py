from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required
from trello.models import User , Board , BoardMember
from flask import request
from . import db



# api to create new board
class CreateBoard(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        title = data.get('title')

        if not title:
            return {"message" : "title required "}, 400
        
        user_id = get_jwt_identity()
        new_board = Board(board_title = title)
        db.session.add(new_board)
        db.session.flush()

        membership = BoardMember(user_id = user_id , board_id = new_board.id , role = 'admin')
        db.session.add(membership)
        db.session.commit()

        return {"message" : f"Board {title} created successfully", "board_id" : new_board.id}

#api to get  board
class GetBoard(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        memberships = BoardMember.query.filter_by(user_id = user_id).all()
        boards = [membership.board for membership in memberships]

        return{
            "boards" : [{"id" : board.id, "title" : board.board_title} for board in boards]
        }