import unittest
from .classboard import Board 

class TestBoard(unittest.TestCase):
    
    def test_str_board(self):
        board = Board()
        expected_board = (
            "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n"  # Fila 7
            "♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n"  # Fila 6
            "                \n"  # Fila 5
            "                \n"  # Fila 4
            "                \n"  # Fila 3
            "                \n"  # Fila 2
            "♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟\n"  # Fila 1
            "♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜\n"  # Fila 0
        )
        self.assertEqual(str(board), expected_board)

    def test_move_piece(self):
        board = Board()
        board.move_piece((1, 1), (3, 1))  # Mover peón blanco de (1,1) a (3,1)
        expected_board = (
            "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n"  # Fila 7
            "♙ ♙ ♙ ♙ ♙ ♙ ♙   \n"  # Fila 6
            "                \n"  # Fila 5
            "                \n"  # Fila 4 (Peón movido a (3,7))
            "               ♟\n"  # Fila 3
            "                \n"  # Fila 2
            "♟ ♟ ♟ ♟ ♟ ♟ ♟   \n"  # Fila 1
            "♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜\n"  # Fila 0
        )
        self.assertEqual(str(board), expected_board)

    def test_get_piece(self):
        board = Board()
        self.assertEqual(
            board.get_piece(1, 1).symbol,
            '♟'  # El peón blanco debe estar en (1,1)
        )

    def test_get_possible_moves(self):
        board = Board()
        # Prueba de movimientos de un peón blanco en (1,1)
        possible_moves = board.get_possible_moves(1, 1)
        self.assertEqual(possible_moves, [(2, 1)])  # Peón puede avanzar una posición



if __name__ == '__main__':
    unittest.main()
