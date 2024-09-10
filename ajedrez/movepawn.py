from .classpieces import Piece

class Pawn(Piece):
    def __init__(self, color='♟'):
        super().__init__(color)  

    def __str__(self):
        if self.__get_color__() == "WHITE":
            return "♟"
        else:
            return "♙"
        
    def get_possible_moves(self, position, board):
        possible_moves = []
        row, col = position
        direction = -1 if self.__get_color__() == "WHITE" else 1
        
        # hacia adelante
        next_row = row + direction
        if 0 <= next_row < 8 and board.get_piece(next_row, col) is None:
            possible_moves.append((next_row, col))
            
            # doble hacia adelante desde p.i
            if (self.get_color() == "WHITE" and row == 6) or (self.get_color() == "BLACK" and row == 1):
                double_row = next_row + direction
                if board.get_piece(double_row, col) is None:
                    possible_moves.append((double_row, col))

        # diagonales
        for diagonal_col in [col - 1, col + 1]:
            if 0 <= diagonal_col < 8:
                target_piece = board.get_piece(next_row, diagonal_col)
                if target_piece and target_piece.get_color() != self.get_color():
                    possible_moves.append((next_row, diagonal_col))
        
        return possible_moves