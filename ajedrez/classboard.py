from classpieces import Rook, Knight, Pawn, Bishop, King, Queen

class Board:
    def __init__(self, size=8):
         self.__size__ = size
         self.__grid__ = [[None for _ in range(size)] for _ in range(size)]
         self._setup_board()


    def _setup_board(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.positions[7][0] = Rook ('♖')
        self.positions[0][0] = Rook ('♜')
        self.positions[7][7] = Rook ('♖')
        self.positions[0][7] = Rook ('♜')
        self.positions[7][1] = Knight ('♘')
        self.positions[7][6] = Knight ('♘')
        self.positions[0][1] = Knight ('♞')
        self.positions[0][6] = Knight ('♞')

        for i in range(8):
            self.positions[6][i] = Pawn('WHITE')
            self.positions[1][i] = Pawn('BLACK')

        self.positions[0][2] = Bishop ('♝')
        self.positions[0][5] = Bishop ('♝')
        self.positions[7][2] = Bishop ('♗')
        self.positions[7][5] = Bishop ('♗')        
        self.positions[7][4] = King ('♕')
        self.positions[7][3] = Queen ('♔')
        self.positions[0][4] = King ('♛')
        self.positions[0][3] = Queen ('♚')      

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            row_str = ""
            for piece in row:
                if piece is None:
                    row_str += "  "
                else:
                    row_str += str(piece) + " "
            board_str += row_str.strip() + "\n"
        return board_str.strip()

    def get_piece(self, row, col):
        return self.__positions__[row][col]