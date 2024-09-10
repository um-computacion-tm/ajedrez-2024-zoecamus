from classpieces import Piece

class Rook(Piece):
    def __init__(self, color, board=None):
        super().__init__(color, board)
        self.symbol = '♜' if color == 'WHITE' else '♖'

    def __str__(self):
        return self.symbol


    def get_possible_moves(self, position, board):
        row, col = position
        possible_moves = []

        # Movimientos verticales
        for direction in [(1, 0), (-1, 0)]:
            for i in range(1, 8):
                new_row = row + direction[0] * i
                new_col = col + direction[1] * i
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target_piece = board.get_piece(new_row, new_col)
                    if target_piece is None:
                        possible_moves.append((new_row, new_col))
                    elif target_piece.get_color() != self.get_color():
                        possible_moves.append((new_row, new_col))
                        break
                    else:
                        break
                else:
                    break

        # Movimientos horizontales
        for direction in [(0, 1), (0, -1)]:
            for i in range(1, 8):
                new_row = row + direction[0] * i
                new_col = col + direction[1] * i
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target_piece = board.get_piece(new_row, new_col)
                    if target_piece is None:
                        possible_moves.append((new_row, new_col))
                    elif target_piece.get_color() != self.get_color():
                        possible_moves.append((new_row, new_col))
                        break
                    else:
                        break
                else:
                    break

        return possible_moves 