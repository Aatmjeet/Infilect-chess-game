class Bishop:

    def __init__(self, bishop):
        self.position = bishop

    def get_moves(self):
        moves = []
        i = int(self.position[1]) - 1  # rows are numbers
        j = ord(self.position[0])  # columns are letters
        temp_i = i
        temp_j = j
        while j > 65 and i < 7:
            j = j - 1
            i = i + 1
        while i >= 0 and j <= 72:
            if i == temp_i and j == temp_j:
                i = i - 1
                j = j + 1
                continue
            pos = chr(j) + str(i + 1)
            moves.append(pos)
            i = i - 1
            j = j + 1

        # diagonal right to left
        i = temp_i
        j = temp_j
        while i < 7 and j < 72:
            i += 1
            j += 1
        while j >= 65 and i >= 0:
            if i == temp_i and j == temp_j:
                i = i - 1
                j = j - 1
                continue
            pos = chr(j) + str(i + 1)
            moves.append(pos)
            i = i - 1
            j = j - 1

        return moves
