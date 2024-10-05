from .classpieces import Pawn

class Pawn(Pawn):
    def get_possible_moves(self, position, board):
        possible_moves = []
        row, col = position
        direction = -1 if self.get_color() == "WHITE" else 1  # Movimiento hacia arriba (blanco) o abajo (negro)

        # Movimiento hacia adelante (una casilla)
        if 0 <= row + direction < 8 and board.is_empty(row + direction, col):
            possible_moves.append((row + direction, col))

        # Movimiento hacia adelante (dos casillas) solo desde la fila inicial
        start_row = 6 if self.get_color() == "WHITE" else 1
        if row == start_row and board.is_empty(row + direction, col) and board.is_empty(row + 2 * direction, col):
            possible_moves.append((row + 2 * direction, col))

        # Captura en diagonal
        for dx in [-1, 1]:
            if 0 <= col + dx < 8 and board.is_enemy_piece(row + direction, col + dx, self.get_color()):
                possible_moves.append((row + direction, col + dx))

        return possible_moves
