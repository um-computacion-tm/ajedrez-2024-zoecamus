from pieces import Rook, Knight, Pawn, Bishop

class Board:
    def __init__(self, size=8):
         self.size = size
         self.grid = [[None for _ in range(size)] for _ in range(size)]
         self._setup_board()
    
         self.positions = []
         for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.positions.append(col)
         self.positions[7][0] = Rook ('♖')
         self.positions[0][0] = Rook ('♜')
         self.positions[7][7] = Rook ('♖')
         self.positions[0][7] = Rook ('♜')
 
         self.positions[7][1] = Knight ('♘')
         self.positions[7][6] = Knight ('♘')
         self.positions[0][1] = Knight ('♞')
         self.positions[0][6] = Knight ('♞')
         
         self.positions[6][0] = Pawn ('♙')
         self.positions[6][1] = Pawn ('♙')
         self.positions[6][2] = Pawn ('♙')
         self.positions[6][3] = Pawn ('♙')
         self.positions[6][4] = Pawn ('♙')
         self.positions[6][5] = Pawn ('♙')  
         self.positions[6][6] = Pawn ('♙')
         self.positions[6][7] = Pawn ('♙')
 
         self.positions[1][0] = Pawn ('♟')
         self.positions[1][1] = Pawn ('♟')
         self.positions[1][2] = Pawn ('♟')
         self.positions[1][3] = Pawn ('♟')
         self.positions[1][4] = Pawn ('♟')
         self.positions[1][5] = Pawn ('♟')  
         self.positions[1][6] = Pawn ('♟')
         self.positions[1][7] = Pawn ('♟')
 
         self.positions[0][2] = Bishop ('♝')
         self.positions[0][5] = Bishop ('♝')
         self.positions[7][2] = Bishop ('♗')
         self.positions[7][5] = Bishop ('♗')
     
    def __str__(self):
        board_str = ""
        symbols = {
            'white': {'Rook': '♖', 'Pawn': '♙'},
            'black': {'Rook': '♜', 'Pawn': '♟'},
        }
        for row in self.grid:
            row_str = ""
            for col in row:
                if col is None:
                    row_str += "  "
                else:
                    piece_type = col.__class__.__name__  # Obtiene el tipo de pieza (Rook, Pawn, etc.)
                    piece_color = col.get_color()  # Accede al color con el método
                    row_str += symbols[piece_color][piece_type] + " "
            board_str += row_str.strip() + "\n"
        return board_str.strip()

        
    def get_piece(self, row, col):
        return self.board.__positions__[row][col]