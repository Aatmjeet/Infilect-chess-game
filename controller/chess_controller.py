from pieces import Bishop, Knight, Rook, Queen


class ChessController:

    @staticmethod
    def get_valid_moves(positions, slug):
        response = dict()
        response['queen'] = Queen(positions["Queen"]).get_moves()
        response['bishop'] = Bishop(positions["Bishop"]).get_moves()
        response['rook'] = Rook(positions["Rook"]).get_moves()
        response['knight'] = Knight(positions["Knight"]).get_moves()

        target_set = set(response[slug])
        response.pop(slug, None)
        opponent_moves = []

        for key, value in response.items():
            opponent_moves = opponent_moves + value

        target_set = target_set.difference(set(opponent_moves))
        return {"valid_moves": sorted(list(target_set))}




