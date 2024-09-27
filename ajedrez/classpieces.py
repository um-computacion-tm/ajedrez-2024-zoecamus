class Piece:

    def __init__(self, color, board=None):
        self.__color__ = color
        self.__board__ = board

    def get_color(self):
        return self.__color__
      
    def __str__(self):
        raise NotImplementedError("Subclasses should implement this method")

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        if self.get_color() == "WHITE":
            return "♜"
        else:
            return "♖"
        
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        if self.get_color() == "WHITE":
            return "♟"
        else:
            return "♙"
        
class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        if self.get_color() == "WHITE":
            return "♞"
        else:
            return "♘"
        
class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        if self.get_color() == "WHITE":
            return "♝"
        else:
            return "♗"
        
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        if self.get_color() == "WHITE":
            return "♛"
        else:
            return "♕"
        
class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        if self.get_color() == "WHITE":
            return "♚"
        else:
            return "♔" 
        
