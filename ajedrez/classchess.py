class Chess:

    def __init__(self, board):
        self.__board__ = board()
        self.__turn__ = 'WHITE'
        
    def is_playing(self):
        return True

    def move(self, 
        from_row, 
        from_col, to_row, to_col):
        
        piece = self.__board__.__get_piece__(from_row, from_col)
        self.change_turn()

    @property
    def turn(self):
        return self.__turn__
    
    def show_board(self):
        return str(self.__board__)
    
    def change_turn(self):
        if self.__turn__ == 'WHITE':
            self.__turn__ = 'BLACK'
        else:
            self.__turn__ = 'WHITE'

class InvalidMove(Exception):
    pass