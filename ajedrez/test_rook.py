import unittest
from .classboard import Board
from .moverook import Rook
from .classpieces import Pawn, Rook

class TestRook(unittest.TestCase):

    def test_str_white_rook(self):
        rook = Rook("WHITE")
        self.assertEqual(str(rook), "♜")
    
    def test_str_black_rook(self):
        rook = Rook("BLACK")
        self.assertEqual(str(rook), "♖")

    def test_move_vertical_desc(self):
        board = Board()
        rook = Rook("WHITE")
        board.set_piece(4, 1, rook)
        possibles = rook.get_possible_moves((4, 1), board)
        expected = [(5, 1), (6, 1), (7, 1)]
        self.assertEqual(possibles, expected)

    def test_move_vertical_asc(self):
        board = Board()
        rook = Rook("WHITE")
        board.set_piece(4, 1, rook)
        possibles = rook.get_possible_moves((4, 1), board)
        expected = [(3, 1), (2, 1), (1, 1), (0, 1)]
        self.assertEqual(possibles, expected)
        
   
    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Rook)
        rook = Rook("WHITE")
        board.set_piece(4, 1, rook)
        possibles = rook.get_possible_moves((4, 1), board)
        expected = [(5, 1)]
        self.assertEqual(possibles, expected)


    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        opponent_pawn = Pawn("BLACK")
        rook = Rook("WHITE")
        board.set_piece(4, 1, rook)
        board.set_piece(6, 1, opponent_pawn)
        possibles = rook.get_possible_moves((4, 1), board)
        expected = [(5, 1), (6, 1)]
        self.assertEqual(possibles,expected)
        
 
if __name__ == '__main__':
    unittest.main()