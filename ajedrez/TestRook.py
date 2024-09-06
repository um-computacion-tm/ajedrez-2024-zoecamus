import unittest
from classboard import Board
from pieces import Rook, Pawn
from rook import Rook


class TestRook(unittest.TestCase):

    def test_str_white_rook(self):
        rook = Rook("WHITE")
        self.assertEqual(str(rook), "♜")

 
if __name__ == '__main__':
    unittest.main()