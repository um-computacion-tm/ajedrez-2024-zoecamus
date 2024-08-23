from pieces import Piece

class Rook(Piece):
    def __init__(self, color='♜'):
        self.__color__ = color
    def __str__(self, __color__):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"
        
class Pawn(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♟"
        else:
            return "♙"
        
class Knight(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♞"
        else:
            return "♘"
        
class Bishop(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♝"
        else:
            return "♗"
        
class Queen(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♛"
        else:
            return "♕"
        
class King(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♚"
        else:
            return "♔" 
        
