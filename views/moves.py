from flask import request
from flask_restful import Resource
from controller.chess_controller import ChessController


class Moves(Resource):
	def post(self, slug):
		data = request.get_json()
		positions = data["positions"]

		valid_moves = ChessController.get_valid_moves(positions=positions, slug=slug)

		return valid_moves, 200
