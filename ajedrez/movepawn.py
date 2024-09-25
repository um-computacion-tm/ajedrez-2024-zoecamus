from .classpieces import Pawn

class MovePawn(Pawn):
    def get_possible_moves(self, position, board):
        possible_moves = []
        col, row = position
        direction = -1 if self.get_color() == "WHITE" else 1  # Movimiento hacia arriba o abajo

        # Movimiento hacia adelante
        if (col, row + direction) in board.get_empty_cells():
            possible_moves.append((col, row + direction))

        # Captura en diagonal
        for dx in [-1, 1]:
            if (col + dx, row + direction) in board.get_opponent_pieces(self.get_color()):
                possible_moves.append((col + dx, row + direction))

        return possible_moves