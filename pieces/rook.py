class Rook:
    def __init__(self, rook):
        self.position = rook

    def get_moves(self):
        moves = []
        # vertical straight
        for i in range(1, 9):
            if str(i) == self.position[1]:
                continue
            pos = self.position[0] + str(i)
            moves.append(pos)

        # horizontal straight
        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            if i == self.position[0]:
                continue
            pos = i + self.position[1]
            moves.append(pos)

        return moves
