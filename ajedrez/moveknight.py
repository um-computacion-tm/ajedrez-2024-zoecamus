from classpieces import Piece

class Knight(Piece):
    def __init__(self, color='♞'):
        super().__init__(color)
    
    def __str__(self):
        if self.__get_color__() == "WHITE":
            return "♞"
        else:
            return "♘"

    def get_possible_moves(self, position, board):
        row, col = position
        possible_moves = []
        
        # movimientos posibles en "L" 
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        for move in knight_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8: 
                t_piece = board.get_piece(new_row, new_col) #target_piece
                if t_piece is None or t_piece.get_color() != self.get_color():
                    possible_moves.append((new_row, new_col))
        
        return possible_moves