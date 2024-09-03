import unittest
from classboard import Board
from pieces import Rook, Pawn
from rook import Rook
class TestBoard(unittest.TestCase):
    
    def test_str_board(self):
        board = Board()
        expected_board = (
            (
                "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n" #Fila 8
                "♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n" #Fila 7
                "               \n" #Fila 6
                "               \n" #Fila 5
                "               \n" #Fila 4
                "               \n" #Fila 3
                "♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟\n" #Fila 2
                "♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜\n" #Fila 1
            )
        )
        self.assertEqual(str(board), expected_board)

    def test_move_piece(self):
        board = Board(8)
        board.move_piece((1, 7), (3, 7))  # Mover peón blanco de F2, a F4
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
        board = Board(8)
        self.assertEqual(
            board.get_piece(1,1),
            Rook('♜')
        )

    def get_possible_moves(self):
        board = Board(8)
        self.assertEqual(
            board.get_possible_moves(1,1),
            [(2,1)]
        )


class TestRook(unittest.TestCase):

    def test_str(self):
        board = Board()
        rook = Rook("WHITE", board)
        self.assertEqual(
            str(rook),
            "♜",
        )

    def test_move_vertical_desc(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1), (7, 1)]
        )

    def test_move_vertical_asc(self):
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1), (1, 1), (0, 1)]
        )

    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )
if __name__ == '__main__':
    unittest.main()