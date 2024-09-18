from .classpieces import Piece

class Queen(Piece):
    def __init__(self, color, board=None):
        super().__init__(color, board)
        self.symbol = '♕' if color == 'WHITE' else '♛'

    def __str__(self):
        return self.symbol

    def get_possible_moves(self, position, board):
        row, col = position
        possible_moves = []

        # Movimientos verticales hacia arriba
        for i in range(row - 1, -1, -1):
            target_piece = board.get_piece(i, col)
            if target_piece is None:
                possible_moves.append((i, col))
            elif target_piece.get_color() != self.get_color():
                possible_moves.append((i, col))
                break
            else:
                break

        # Movimientos verticales hacia abajo
        for i in range(row + 1, 8):
            target_piece = board.get_piece(i, col)
            if target_piece is None:
                possible_moves.append((i, col))
            elif target_piece.get_color() != self.get_color():
                possible_moves.append((i, col))
                break
            else:
                break

        # Movimientos horizontales hacia la derecha
        for i in range(col + 1, 8):
            target_piece = board.get_piece(row, i)
            if target_piece is None:
                possible_moves.append((row, i))
            elif target_piece.get_color() != self.get_color():
                possible_moves.append((row, i))
                break
            else:
                break

        # Movimientos horizontales hacia la izquierda
        for i in range(col - 1, -1, -1):
            target_piece = board.get_piece(row, i)
            if target_piece is None:
                possible_moves.append((row, i))
            elif target_piece.get_color() != self.get_color():
                possible_moves.append((row, i))
                break
            else:
                break

        # Movimientos diagonales hacia la esquina superior izquierda
        for i in range(1, min(row, col) + 1):
            target_piece = board.get_piece(row - i, col - i)
            if target_piece is None:
                possible_moves.append((row - i, col - i))
            elif target_piece.get_color() != self.get_color():
                possible_moves.append((row - i, col - i))
                break
            else:
                break

        # Movimientos diagonales hacia la esquina superior derecha
        for i in range(1, min(row, 7 - col) + 1):
            target_piece = board.get_piece(row - i, col + i)
            if target_piece is None:
                possible_moves.append((row - i, col + i))
            elif target_piece.get_color() != self.get_color():
                possible_moves.append((row - i, col + i))
                break
            else:
                break

        # Movimientos diagonales hacia la esquina inferior izquierda
        for i in range(1, min(7 - row, col) + 1):
            target_piece = board.get_piece(row + i, col - i)
            if target_piece is None:
                possible_moves.append((row + i, col - i))
            elif target_piece.get_color() != self.get_color():
                possible_moves.append((row + i, col - i))
                break
            else:
                break

        # Movimientos diagonales hacia la esquina inferior derecha
        for i in range(1, min(7 - row, 7 - col) + 1):
            target_piece = board.get_piece(row + i, col + i)
            if target_piece is None:
                possible_moves.append((row + i, col + i))
            elif target_piece.get_color() != self.get_color():
                possible_moves.append((row + i, col + i))
                break
            else:
                break

        return possible_moves