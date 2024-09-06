class Piece:

    def __init__(self, color, board=None):
        self.__color__ = color
        self.__board__ = board

    def get_color(self):
        return self.__color__


    def get_possible_moves(self, position, board):
        posibles_moves = []
        col, row = position
        for i in range(1, 8):
            if (col + i, row) in board.get_empty_cells():
                posibles_moves.append((col + i, row))
        return posibles_moves 
      
    def __str__(self):
        raise NotImplementedError("Subclasses should implement this method")
    
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

class Bishop(Piece):
    def __init__(self, color, board=None):
        super().__init__(color, board)
        self.symbol = '♝' if color == 'WHITE' else '♗'

    def __str__(self):
        return self.symbol

    def get_possible_moves(self, position):
        row, col = position
        possible_moves = []
class Queen(Piece):
    ...
class King(Piece):
    ... 