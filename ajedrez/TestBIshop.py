import unittest
from classboard import Board
from pieces import Bishop

class TestBishop(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()

    def test_move_diagonal_up_left(self):
        bishop = Bishop('WHITE', self.board)
        self.board.positions[3][3] = bishop
        possible_moves = bishop.get_possible_moves((3, 3))

        expected_moves = [(2, 2), (1, 1), (0, 0)]
        self.assertEqual(possible_moves, expected_moves)

if __name__ == "__main__":
    unittest.main()
