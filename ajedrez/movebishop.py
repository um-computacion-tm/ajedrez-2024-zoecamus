from .classpieces import Piece

class Bishop(Piece):
    def __init__(self, color, board=None):
        super().__init__(color, board)
        self.symbol = '♝' if color == 'WHITE' else '♗'

    def __str__(self):
        return self.symbol

    def get_possible_moves(self, position, board):
        row, col = position
        possible_moves = []

        for i in range(1, min(row, col) + 1):
            if self.board.positions[row - i][col - i] is None:
                possible_moves.append((row - i, col - i))
            elif self.board.positions[row - i][col - i].get_color() != self.get_color():
                possible_moves.append((row - i, col - i))
                break
            else:
                break
        for i in range(1, min(row, 7 - col) + 1):
            if self.board.positions[row - i][col + i] is None:
                possible_moves.append((row - i, col + i))
            elif self.board.positions [row - i][col + i].get_color() != self.get_color():
                possible_moves.append((row - i, col + i))
                break
            else:
                break

        for i in range(1, min(7 - row, col) + 1):
            if self.board.positions[row + i][col - i] is None:
                possible_moves.append((row + i, col - i))
            elif self.board.positions[row + i][col - i].get_color() != self.get_color():
                possible_moves.append((row + i, col - i))
                break
            else:
                break
        
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