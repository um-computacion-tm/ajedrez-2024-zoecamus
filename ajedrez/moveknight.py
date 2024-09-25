from .classpieces import Knight

class Knight(Knight):
    def get_possible_moves(self, position, board):
        row, col = position
        possible_moves = []

        moves = [
            (row - 2, col - 1), (row - 2, col + 1),
            (row - 1, col - 2), (row - 1, col + 2),
            (row + 1, col - 2), (row + 1, col + 2),
            (row + 2, col - 1), (row + 2, col + 1),
        ]

        for move in moves:
            if board.is_empty_or_enemy(move[0], move[1], self.get_color()):
                possible_moves.append(move)

        return possible_moves