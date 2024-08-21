from pieces import Rook

class Board:
    def __init__(self, size):
        self.positions = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.positions.append(col)
        self.positions[0][0] = Rook('BLACK')
        self.positions[7][7] = Rook('WHITE')
        self.positions[0][7] = Rook('BLACK')
        self.positions[7][0] = Rook('WHITE')


    def __str__(self):
        board_str = ''
        for row in self.positions:
            for col in row:
                if col is not None:
                    board_str += col.color
                else:
                    board_str += ''
            board_str += '\n'

            
    def get_piece(self, row, col):
        return self.board.__positions__[row][col]