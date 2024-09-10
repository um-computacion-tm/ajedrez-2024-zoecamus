import unittest
from classboard import Board
from moverook import Rook
from ajedrez.classpieces import Rook


class TestBoard(unittest.TestCase):
    
    def test_str_board(self):
        board = Board()
        expected_board = (
            (
                "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n" #Fila 7
                "♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n" #Fila 6
                "               \n" #Fila 5
                "               \n" #Fila 4
                "               \n" #Fila 3
                "               \n" #Fila 2
                "♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟\n" #Fila 1
                "♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜\n" #Fila 0
            )
        )
        self.assertEqual(str(board), expected_board)

    def test_move_piece(self):
        board = Board()
        board.move_piece((1, 7), (3, 7))  # Mover peón blanco de F1, a F3
        expected_board = (
            (
                "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n" #Fila 7
                "♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n" #Fila 6
                "               \n" #Fila 5
                "               \n" #Fila 4
                "♟              \n" #Fila 3
                "               \n" #Fila 2
                "  ♟ ♟ ♟ ♟ ♟ ♟ ♟\n" #Fila 1
                "♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜\n" #Fila 0
  
            )
         
        )
        self.assertEqual(str(board), expected_board)


    def test_get_piece(self):
        board = Board()
        self.assertEqual(
            board.get_piece(1,1),
            Rook('♜')
        )

    def get_possible_moves(self):
        board = Board()
        self.assertEqual(
            board.get_possible_moves(1,1),
            [(2,1)]
        )


if __name__ == '__main__':
    unittest.main()