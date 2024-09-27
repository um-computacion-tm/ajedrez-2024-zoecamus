import unittest
from .classboard import Board
from .movequeen import Queen

class TestQueen(unittest.TestCase):

    def test_str_white_queen(self):
        queen = Queen("WHITE")
        self.assertEqual(str(queen), "♛")

    def test_str_black_queen(self):
        queen = Queen("BLACK")
        self.assertEqual(str(queen), "♕")
        
    def setUp(self):
        self.board = Board()
        self.queen_white = Queen("WHITE")
        self.queen_black = Queen("BLACK")

    def test_queen_initial_position_white(self):
        # La reina blanca está en la posición inicial (7, 3)
        self.board.setup_initial_board()
        moves = self.queen_white.get_possible_moves((7, 3), self.board)
        
        expected_moves = [
            # Verticales
            (6, 3), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (0, 3),
            # Horizontales
            (7, 2), (7, 1), (7, 0), (7, 4), (7, 5), (7, 6), (7, 7),
            # Diagonales
            (6, 2), (5, 1), (4, 0), (6, 4), (5, 5), (4, 6), (3, 7)
        ]
        self.assertEqual(sorted(moves), sorted(expected_moves))

    def test_queen_mid_board_white(self):
        # Reina blanca en el centro del tablero
        self.board.clear_board()
        self.board.place_piece((4, 4), "QUEEN", "WHITE")
        moves = self.queen_white.get_possible_moves((4, 4), self.board)
        
        expected_moves = [
            # Verticales
            (5, 4), (6, 4), (7, 4), (3, 4), (2, 4), (1, 4), (0, 4),
            # Horizontales
            (4, 5), (4, 6), (4, 7), (4, 3), (4, 2), (4, 1), (4, 0),
            # Diagonales
            (5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1), 
            (3, 3), (2, 2), (1, 1), (0, 0), (3, 5), (2, 6), (1, 7)
        ]
        self.assertEqual(sorted(moves), sorted(expected_moves))

    def test_queen_blocked_by_own_pieces(self):
        # La reina está rodeada por sus propias piezas
        self.board.clear_board()
        self.board.place_piece((4, 4), "QUEEN", "WHITE")
        self.board.place_piece((5, 4), "PAWN", "WHITE")  # Bloqueando arriba
        self.board.place_piece((4, 5), "PAWN", "WHITE")  # Bloqueando derecha
        self.board.place_piece((3, 4), "PAWN", "WHITE")  # Bloqueando abajo
        self.board.place_piece((4, 3), "PAWN", "WHITE")  # Bloqueando izquierda
        
        moves = self.queen_white.get_possible_moves((4, 4), self.board)
        expected_moves = [
            (5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1), 
            (3, 5), (2, 6), (1, 7), (3, 3), (2, 2), (1, 1), (0, 0)
        ]  # Solo movimientos diagonales
        self.assertEqual(sorted(moves), sorted(expected_moves))

    def test_queen_can_capture_enemy(self):
        # La reina puede capturar una pieza enemiga
        self.board.clear_board()
        self.board.place_piece((4, 4), "QUEEN", "WHITE")
        self.board.place_piece((5, 4), "PAWN", "BLACK")  # Enemigo en el camino

        moves = self.queen_white.get_possible_moves((4, 4), self.board)
        expected_moves = [
            # Verticales
            (5, 4), (3, 4), (2, 4), (1, 4), (0, 4),
            # Horizontales
            (4, 5), (4, 6), (4, 7), (4, 3), (4, 2), (4, 1), (4, 0),
            # Diagonales
            (5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1), 
            (3, 3), (2, 2), (1, 1), (0, 0), (3, 5), (2, 6), (1, 7)
        ]
        self.assertEqual(sorted(moves), sorted(expected_moves))

if __name__ == '__main__':
    unittest.main()
