import unittest
from ajedrez.classboard import Board
from ajedrez.movebishop import Bishop

class TestBishop(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()

    def test_move_diagonal_up_left(self):
        bishop = Bishop('WHITE', self.board)
        self.board.positions[3][3] = bishop
        possible_moves = bishop.get_possible_moves((3, 3))

        expected_moves = [(2, 2), (1, 1), (0, 0)]
        self.assertEqual(possible_moves, expected_moves)

    def test_move_diagonal_up_right(self):
        bishop = Bishop('WHITE', self.board)
        self.board.positions[3][3] = bishop
        possible_moves = bishop.get_possible_moves((3, 3))

        expected_moves = [(2, 2), (1, 1), (0, 0), (2, 4), (1, 5), (0, 6)]
        self.assertEqual(possible_moves, expected_moves)




if __name__ == "__main__":
    unittest.main()
