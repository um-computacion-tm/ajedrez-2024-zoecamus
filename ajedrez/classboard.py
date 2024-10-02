from .classpieces import Rook, Knight, Pawn, Bishop, King, Queen

class Board:
    def __init__(self, size=8):
        self.__size__ = size
        self.__grid__ = [[None for _ in range(size)] for _ in range(size)]
        self._setup_board()

    def _setup_board(self):
        # Inicializar posiciones vacías
        self.__positions__ = []
        for _ in range(self.__size__):
            col = [None for _ in range(self.__size__)]
            self.__positions__.append(col)

        # Colocar las torres
        self.__positions__[7][0] = Rook('WHITE')  # ♜
        self.__positions__[7][7] = Rook('WHITE')  # ♜
        self.__positions__[0][0] = Rook('BLACK')  # ♖
        self.__positions__[0][7] = Rook('BLACK')  # ♖

        # Colocar los caballos
        self.__positions__[7][1] = Knight('WHITE')  # ♞
        self.__positions__[7][6] = Knight('WHITE')  # ♞
        self.__positions__[0][1] = Knight('BLACK')  # ♘
        self.__positions__[0][6] = Knight('BLACK')  # ♘

        # Colocar los alfiles
        self.__positions__[7][2] = Bishop('WHITE')  # ♝
        self.__positions__[7][5] = Bishop('WHITE')  # ♝
        self.__positions__[0][2] = Bishop('BLACK')  # ♗
        self.__positions__[0][5] = Bishop('BLACK')  # ♗

        # Colocar los peones
        for i in range(8):
            self.__positions__[6][i] = Pawn('WHITE')  # ♟
            self.__positions__[1][i] = Pawn('BLACK')  # ♙

        # Colocar las reinas
        self.__positions__[7][3] = Queen('WHITE')  # ♚
        self.__positions__[0][3] = Queen('BLACK')  # ♔

        # Colocar los reyes
        self.__positions__[7][4] = King('WHITE')  # ♛
        self.__positions__[0][4] = King('BLACK')  # ♕

    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            row_str = ""
            for piece in row:
                if piece is None:
                    row_str += " . "  # Casilla vacía
                else:
                    row_str += f" {str(piece)} "  # Representación de la pieza
            board_str += row_str.strip() + "\n"
        return board_str.strip()

    def get_piece(self, row, col):
        """Devuelve la pieza en la posición especificada, o Non"""
        if 0 <= row < self.__size__ and 0 <= col < self.__size__:
            return self.__positions__[row][col]
        return None

    def set_piece(self, row, col, piece):
        """Coloca una pieza en una posición específica del tablero."""
        if 0 <= row < self.__size__ and 0 <= col < self.__size__:
            self.__positions__[row][col] = piece

    def get_empty_cells(self):
        """Devuelve una lista de todas las casillas vacías en el tablero."""
        empty_cells = []
        for row in range(self.__size__):
            for col in range(self.__size__):
                if self.__positions__[row][col] is None:
                    empty_cells.append((row, col))
        return empty_cells