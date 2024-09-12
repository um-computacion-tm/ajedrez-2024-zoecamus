from .classpieces import Rook, Knight, Pawn, Bishop, King, Queen

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
        self.__positions__[7][0] = Rook ('♖')
        self.__positions__[0][0] = Rook ('♜')
        self.__positions__[7][7] = Rook ('♖')
        self.__positions__[0][7] = Rook ('♜')
        self.__positions__[7][1] = Knight ('♘')
        self.__positions__[7][6] = Knight ('♘')
        self.__positions__[0][1] = Knight ('♞')
        self.__positions__[0][6] = Knight ('♞')

        for i in range(8):
            self.__positions__[6][i] = Pawn('♟')
            self.__positions__[1][i] = Pawn('♙')

        self.__positions__[0][2] = Bishop ('♝')
        self.__positions__[0][5] = Bishop ('♝')
        self.__positions__[7][2] = Bishop ('♗')
        self.__positions__[7][5] = Bishop ('♗')        
        self.__positions__[7][4] = King ('♕')
        self.__positions__[7][3] = Queen ('♔')
        self.__positions__[0][4] = King ('♛')
        self.__positions__[0][3] = Queen ('♚')      

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
    
    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece