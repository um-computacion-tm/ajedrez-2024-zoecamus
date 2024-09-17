from .classpieces import Piece

class Rook(Piece):
    def __init__(self, color, board=None):
        super().__init__(color, board)
        self.symbol = '♜' if color == 'WHITE' else '♖'

    def __str__(self):
        return self.symbol

    def get_possible_moves(self, position, board):
        row, col = position
        possible_moves = []
  

        # Movimientos verticales ascendentes (hacia arriba)
        for i in range(row - 1, -1, -1):
            target_piece = board.get_piece(i, col)
            if target_piece is None:
                possible_moves.append((i, col))  
            elif target_piece.get_color() != self.get_color():
                possible_moves.append((i, col)) 
                break  
            else:
                break  

        # Movimientos verticales descendentes 
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

        return possible_moves
