import unittest
from .classboard import Board
from .moverook import Bishop
from .classpieces import Pawn, Rook

class TestBishop(unittest.TestCase):

    def test_str_white_bishop(self):
        bishop = Bishop("WHITE")
        self.assertEqual(str(bishop), "♝")

    def test_str_black_bishop(self):
        bishop = Bishop("BLACK")
        self.assertEqual(str(bishop), "♗")

    def test_move_diagonal_top_left(self):
        board = Board()
        bishop = Bishop("WHITE")
        board.set_piece(4, 4, bishop)
        possibles = bishop.get_possible_moves((4, 4), board)
        expected = [(3, 3), (2, 2), (1, 1), (0, 0)]
        self.assertEqual(possibles, expected)

    def test_move_diagonal_top_right(self):
        board = Board()
        bishop = Bishop("WHITE")
        board.set_piece(4, 4, bishop)
        possibles = bishop.get_possible_moves((4, 4), board)
        expected = [(3, 5), (2, 6), (1, 7)]
        self.assertEqual(possibles, expected)

    def test_move_diagonal_bottom_left(self):
        board = Board()
        bishop = Bishop("WHITE")
        board.set_piece(4, 4, bishop)
        possibles = bishop.get_possible_moves((4, 4), board)
        expected = [(5, 3), (6, 2), (7, 1)]
        self.assertEqual(possibles, expected)

    def test_move_diagonal_bottom_right(self):
        board = Board()
        bishop = Bishop("WHITE")
        board.set_piece(4, 4, bishop)
        possibles = bishop.get_possible_moves((4, 4), board)
        expected = [(5, 5), (6, 6), (7, 7)]
        self.assertEqual(possibles, expected)

    def test_move_with_obstacle_own_piece(self):
        board = Board()
        bishop = Bishop("WHITE")
        own_pawn = Pawn("WHITE")
        board.set_piece(4, 4, bishop)
        board.set_piece(2, 2, own_pawn)
        possibles = bishop.get_possible_moves((4, 4), board)
        expected = [(3, 3)]
        self.assertEqual(possibles, expected)

    def test_move_with_obstacle_opponent_piece(self):
        board = Board()
        bishop = Bishop("WHITE")
        opponent_pawn = Pawn("BLACK")
        board.set_piece(4, 4, bishop)
        board.set_piece(2, 2, opponent_pawn)
        possibles = bishop.get_possible_moves((4, 4), board)
        expected = [(3, 3), (2, 2)]
        self.assertEqual(possibles, expected)

if __name__ == '__main__':
    unittest.main()
