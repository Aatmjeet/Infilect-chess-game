class Knight:

    def __init__(self, knight):
        self.position = knight

    def get_moves(self):
        moves = []
        i = int(self.position[1]) - 1
        j = ord(self.position[0])

        # horizontal movement
        if (j - 2) >= 65:
            if (i + 1) <= 7:
                moves.append(chr(j - 2) + str(i+1+1))
            if (i - 1) >= 0:
                moves.append(chr(j - 2) + str(i+1-1))

        if (j + 2) >= 65:
            if (i + 1) <= 7:
                moves.append(chr(j + 2) + str(i + 1 + 1))
            if (i - 1) >= 0:
                moves.append(chr(j + 2) + str(i + 1 - 1))

        # vertical movement
        if (i - 2) >= 0:
            if (j + 1) <= 72:
                moves.append(chr(j + 1) + str(i - 1))
            if (j - 1) >= 65:
                moves.append(chr(j - 1) + str(i - 1))

        if (i + 2) >= 0:
            if (j + 1) <= 72:
                moves.append(chr(j + 1) + str(i + 3))
            if (j - 1) >= 65:
                moves.append(chr(j - 1) + str(i + 3))

        return moves