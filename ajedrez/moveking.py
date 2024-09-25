from .classpieces import King

class King(King):
    def get_possible_moves(self, position, board):
        row, col = position
        possible_moves = []

        moves = [
            (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
            (row, col - 1),                      (row, col + 1),
            (row + 1, col - 1), (row + 1, col), (row + 1, col + 1),
        ]

        for move in moves:
            move_row, move_col = move
            # Verifica que las coordenadas estén dentro del tablero
            if 0 <= move_row < 8 and 0 <= move_col < 8:
                if board.is_empty_or_enemy(move_row, move_col, self.get_color()):
                    possible_moves.append(move)

        return possible_moves
