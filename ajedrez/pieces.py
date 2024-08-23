class Piece:
    def __init__(self, color):
        self.__color__ = color
    def get_color(self):
        return self.__color__

    def get_possible_moves(self, position, board):
        posibles_moves = []
        col, row = position
        for i in range(1, 8):
            if (col + i, row) in board.get_empty_cells():
                posibles_moves.append((col + i, row))
        return posibles_moves   
    

class Rook(Piece): 
      def get_possible_moves(self, position, board):
        row, col = position
        possible_moves = []
      
      # Horizontal and Vertical moves
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in directions:
            for i in range(1, 8):
                new_row = row + direction[0] * i
                new_col = col + direction[1] * i
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    target_piece = board.get_piece(new_row, new_col)
                    if target_piece is None:
                        possible_moves.append((new_row, new_col))
                    elif target_piece.get_color() != self._color:
                        possible_moves.append((new_row, new_col))
                        break
                    else:
                        break
                else:
                    break
        return possible_moves


class Pawn(Piece):
    ...
class Knight(Piece):
    ...
class Bishop(Piece):
    ...
class Queen(Piece):
    ...
class King(Piece):
    ... 