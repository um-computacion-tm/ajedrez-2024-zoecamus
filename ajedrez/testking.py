import unittest
from .classboard import Board
from .moveking import King

class TestKing(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()  # Inicializa el tablero
        self.king = King('WHITE')  # Crea un rey blanco

    def test_king_initial_position(self):
        # Prueba los movimientos desde la posición inicial del rey blanco
        self.board.set_piece(4, 0, self.king)  # Coloca el rey en su posición inicial
        expected_moves = [
            (4, 1), (5, 0), (3, 0), (4, -1), 
            (5, 1), (3, -1), (3, 1), (5, -1)
        ]
        valid_moves = self.king.get_possible_moves((4, 0), self.board)
        self.assertTrue(all(move in expected_moves for move in valid_moves))

    def test_king_edge_position(self):
        # Prueba los movimientos desde una posición en el borde del tablero
        self.board.set_piece(0, 0, self.king)  # Coloca el rey en la esquina
        expected_moves = [
            (1, 0), (0, 1), (1, 1)
        ]
        valid_moves = self.king.get_possible_moves((0, 0), self.board)
        self.assertTrue(all(move in expected_moves for move in valid_moves))

    def test_king_capture_opponent_piece(self):
        # Prueba los movimientos al capturar una pieza opuesta
        opponent_piece = King('BLACK')
        self.board.set_piece(4, 1, opponent_piece)  # Coloca una pieza negra en el rango del rey
        self.board.set_piece(4, 0, self.king)  # Coloca el rey blanco en su posición inicial
        expected_moves = [
            (4, 1), (5, 0), (3, 0), (5, 1), (3, 1)
        ]
        valid_moves = self.king.get_possible_moves((4, 0), self.board)
        self.assertTrue(all(move in expected_moves for move in valid_moves))

    def test_king_no_moves(self):
        # Prueba un escenario donde el rey no puede moverse
        self.board.set_piece(0, 0, self.king)  # Coloca el rey en la esquina
        self.board.set_piece(0, 1, King('BLACK'))  # Coloca un rey negro bloqueando
        expected_moves = []  # El rey no puede moverse
        valid_moves = self.king.get_possible_moves((0, 0), self.board)
        self.assertEqual(valid_moves, expected_moves)

if __name__ == '__main__':
    unittest.main()