import unittest
from .classboard import Board
from .classpieces import Pawn, Rook, Knight

class TestBoard(unittest.TestCase):
    
    def test_str_board(self):
        board = Board()
        expected_board = (
            "♜ ♞ ♝ ♚ ♛ ♝ ♞ ♜\n"  # Fila 0 (Negra)
            "♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n"  # Fila 1 (Negra)
            " .  .  .  .  .  .  .  . \n"  # Fila 2 (Vacía)
            " .  .  .  .  .  .  .  . \n"  # Fila 3 (Vacía)
            " .  .  .  .  .  .  .  . \n"  # Fila 4 (Vacía)
            " .  .  .  .  .  .  .  . \n"  # Fila 5 (Vacía)
            "♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟\n"  # Fila 6 (Blanca)
            "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖"   # Fila 7 (Blanca)
        )
        self.assertEqual(str(board), expected_board)

    def test_move_piece(self):
        board = Board()
        pawn = board.get_piece(6, 1)  # Peón blanco en (6,1)
        board.set_piece(4, 1, pawn)  # Mover el peón blanco de (6,1) a (4,1)
        board.set_piece(6, 1, None)  # Quitar el peón de su posición inicial
        
        expected_board = (
            "♜ ♞ ♝ ♚ ♛ ♝ ♞ ♜\n"  # Fila 0 (Negra)
            "♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n"  # Fila 1 (Negra)
            " .  .  .  .  .  .  .  . \n"  # Fila 2 (Vacía)
            " .  .  .  .  .  .  .  . \n"  # Fila 3 (Vacía)
            " .  ♟  .  .  .  .  .  . \n"  # Fila 4 (Peón movido a (4,1))
            " .  .  .  .  .  .  .  . \n"  # Fila 5 (Vacía)
            "♟  . ♟ ♟ ♟ ♟ ♟ ♟\n"  # Fila 6 (Blanca sin peón en (6,1))
            "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖"   # Fila 7 (Blanca)
        )
        self.assertEqual(str(board), expected_board)

    def test_get_piece(self):
        board = Board()
        piece = board.get_piece(6, 0)  # Peón blanco en (6,0)
        self.assertIsInstance(piece, Pawn)
        self.assertEqual(str(piece), '♟')  # Comprobar que es un peón blanco

        rook = board.get_piece(7, 0)  # Torre blanca en (7,0)
        self.assertIsInstance(rook, Rook)
        self.assertEqual(str(rook), '♖')  # Comprobar que es una torre blanca

    def test_get_possible_moves(self):
        board = Board()
        knight = board.get_piece(7, 1)  # Caballo blanco en (7,1)
        possible_moves = knight.get_possible_moves((7, 1), board)
        expected_moves = [(5, 0), (5, 2)]  # Movimientos posibles del caballo
        self.assertEqual(possible_moves, expected_moves)

    def test_get_empty_cells(self):
        board = Board()
        empty_cells = board.get_empty_cells()
        expected_empty_cells = [
            (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
            (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7),
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
            (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7),
        ]
        self.assertEqual(empty_cells, expected_empty_cells)


if __name__ == '__main__':
    unittest.main()