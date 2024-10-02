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
            r, c = move
            if 0 <= r < 8 and 0 <= c < 8:  # Verifica que la posición esté dentro del tablero
                if board.is_empty_or_enemy(r, c, self.get_color()):
                    possible_moves.append(move)

        return possible_moves
