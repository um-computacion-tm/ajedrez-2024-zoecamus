from .classpieces import Piece

class King(Piece):
    def get_moves(self, Board):
        moves = []
        potential_moves = [
            (self.get_row() + 1, self.get_column()),
            (self.get_row() - 1, self.get_column()),
            (self.get_row(), self.get_column() + 1),
            (self.get_row(), self.get_column() - 1),
            (self.get_row() + 1, self.get_column() + 1),
            (self.get_row() + 1, self.get_column() - 1),
            (self.get_row() - 1, self.get_column() + 1),
            (self.get_row() - 1, self.get_column() - 1),
        ]