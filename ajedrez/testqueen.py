import unittest
from .classboard import Board
from .movequeen import Queen
from .classpieces import Pawn

class TestQueen(unittest.TestCase):

    def test_str_white_queen(self):
        queen = Queen("WHITE")
        self.assertEqual(str(queen), "♕")

    def test_str_black_queen(self):
        queen = Queen("BLACK")
        self.assertEqual(str(queen), "♛")

    def test_move_full_range(self):
        board = Board()
        queen = Queen("WHITE")
        board.set_piece(4, 4, queen)
        possibles = queen.get_possible_moves((4, 4), board)
        expected = [
            # Vertical
            (3, 4), (2, 4), (1, 4), (0, 4),
            (5, 4), (6, 4), (7, 4),
            # Horizontal
            (4, 3), (4, 2), (4, 1), (4, 0),
            (4, 5), (4, 6), (4, 7),
            # Diagonal
            (3, 3), (2, 2), (1, 1), (0, 0),
            (3, 5), (2, 6), (1, 7),
            (5, 3), (6, 2), (7, 1),
            (5, 5), (6, 6), (7, 7)
        ]
        self.assertEqual(possibles, expected)

    def test_move_with_obstacle_own_piece(self):
        board = Board()
        queen = Queen("WHITE")
        own_pawn = Pawn("WHITE")
        board.set_piece(4, 4, queen)
        board.set_piece(2, 2, own_pawn)
        possibles = queen.get_possible_moves((4, 4), board)
        expected = [
            # Vertical
            (3, 4), (2, 4), (1, 4), (0, 4),
            (5, 4), (6, 4), (7, 4),
            # Horizontal
            (4, 3), (4, 2), (4, 1), (4, 0),
            (4, 5), (4, 6), (4, 7),
            # Diagonal
            (3, 3)
        ]
        self.assertEqual(possibles, expected)

    def test_move_with_obstacle_opponent_piece(self):
        board = Board()
        queen = Queen("WHITE")
        opponent_pawn = Pawn("BLACK")
        board.set_piece(4, 4, queen)
        board.set_piece(2, 2, opponent_pawn)
        possibles = queen.get_possible_moves((4, 4), board)
        expected = [
            # Vertical
            (3, 4), (2, 4), (1, 4), (0, 4),
            (5, 4), (6, 4), (7, 4),
            # Horizontal
            (4, 3), (4, 2), (4, 1), (4, 0),
            (4, 5), (4, 6), (4, 7),
            # Diagonal
            (3, 3), (2, 2)
        ]
        self.assertEqual(possibles, expected)

if __name__ == '__main__':
    unittest.main()
