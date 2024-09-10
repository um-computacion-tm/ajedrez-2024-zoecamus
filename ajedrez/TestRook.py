import unittest
from classboard import Board
from moverook import Rook
from classpieces import Pawn
from classpieces import Rook


class TestRook(unittest.TestCase):

    def test_str_white_rook(self):
        rook = Rook("WHITE")
        self.assertEqual(str(rook), "♜")
    
    def test_str_black_rook(self):
        rook = Rook("BLACK")
        self.assertEqual(str(rook), "♖")
   
    def test_move_vertical_desc(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.get_possible_moves((4, 1), board)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1), (7, 1)]
        )

    def test_move_vertical_asc(self):
        board = Board()
        rook = Rook("WHITE")
        board.__set_piece__(4, 1, rook)
        possibles = rook.get_possible_moves((4, 1), board)
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1), (1, 1), (0, 1)]
        )

   
    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.__positions__[6][1] = Pawn("WHITE", board)
        rook = Rook("WHITE", board)
        board.__positions__[4][1] = rook
        possibles = rook.get_possible_moves((4, 1), board)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )


    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.positions[6][1] = Pawn("BLACK", board)
        rook = Rook("WHITE", board)
        board.positions[4][1] = rook
        possibles = rook.get_possible_moves((4, 1), board)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )

 
if __name__ == '__main__':
    unittest.main()