import unittest
from .classboard import Board
from .moveknight import Knight

class TestKnight(unittest.TestCase):

    def setUp(self):
        # Configuración básica del tablero y la pieza Caballo
        self.board = Board()
        self.knight_white = Knight("WHITE")
        self.knight_black = Knight("BLACK")
        # Colocar el caballo blanco en la posición (7, 1) y el negro en (0, 1)
        self.board.set_piece((7, 1), self.knight_white)
        self.board.set_piece((0, 1), self.knight_black)

    def test_knight_moves_in_center(self):
        # Mover el caballo blanco al centro del tablero (4, 4) y comprobar sus movimientos
        self.board.set_piece((4, 4), self.knight_white)
        expected_moves = [
            (2, 3), (2, 5),
            (3, 2), (3, 6),
            (5, 2), (5, 6),
            (6, 3), (6, 5)
        ]
        possible_moves = self.knight_white.get_possible_moves((4, 4), self.board)
        self.assertCountEqual(possible_moves, expected_moves)

    def test_knight_moves_on_edge(self):
        # Verificar los movimientos del caballo blanco en la posición (7, 1)
        expected_moves = [
            (5, 0), (5, 2), (6, 3)
        ]
        possible_moves = self.knight_white.get_possible_moves((7, 1), self.board)
        self.assertCountEqual(possible_moves, expected_moves)

    def test_knight_blocked_by_ally(self):
        # Colocar una pieza aliada en una posición de movimiento del caballo
        self.board.set_piece((5, 2), Knight("WHITE"))  # Aliado blanco en (5, 2)
        expected_moves = [
            (5, 0), (6, 3)  # Solo las casillas no bloqueadas por aliados
        ]
        possible_moves = self.knight_white.get_possible_moves((7, 1), self.board)
        self.assertCountEqual(possible_moves, expected_moves)

    def test_knight_capture_enemy(self):
        # Colocar una pieza enemiga en una posición de movimiento del caballo
        self.board.set_piece((5, 2), Knight("BLACK"))  # Enemigo negro en (5, 2)
        expected_moves = [
            (5, 0), (5, 2), (6, 3)  # Puede capturar en (5, 2)
        ]
        possible_moves = self.knight_white.get_possible_moves((7, 1), self.board)
        self.assertCountEqual(possible_moves, expected_moves)

    def test_knight_moves_out_of_bounds(self):
        # Verificar los movimientos del caballo negro en la esquina superior izquierda (0, 1)
        expected_moves = [
            (2, 0), (2, 2), (1, 3)
        ]
        possible_moves = self.knight_black.get_possible_moves((0, 1), self.board)
        self.assertCountEqual(possible_moves, expected_moves)

if __name__ == '__main__':
    unittest.main()
