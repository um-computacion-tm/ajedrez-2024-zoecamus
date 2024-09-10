import unittest
from classboard import Board
from moveknight import Knight

class TestKnight(unittest.TestCase):
    
    def test_knight_initial_position_white(self):
        board = Board()
        knight = Knight("WHITE")
        board.set_piece(0, 1, knight)  # Caballo blanco en su posición inicial en (0, 1)
        
        # Los movimientos esperados del caballo blanco en la posición inicial
        expected_moves = [(2, 0), (2, 2)]
        self.assertEqual(knight.get_possible_moves((0, 1), board), expected_moves)

    def test_knight_initial_position_black(self):
        board = Board()
        knight = Knight("BLACK")
        board.set_piece(7, 1, knight)  # Caballo negro en su posición inicial en (7, 1)
        
        # Los movimientos esperados del caballo negro en la posición inicial
        expected_moves = [(5, 0), (5, 2)]
        self.assertEqual(knight.get_possible_moves((7, 1), board), expected_moves)

    def test_knight_blocked_by_own_pieces(self):
        board = Board()
        knight = Knight("WHITE")
        board.set_piece(0, 1, knight)  # Caballo blanco en su posición inicial en (0, 1)
        board.set_piece(2, 0, Knight("WHITE"))  # Caballo blanco bloqueando movimiento
        board.set_piece(2, 2, Knight("WHITE"))  # Caballo blanco bloqueando movimiento
        
        # Movimientos bloqueados por otras piezas blancas
        expected_moves = []
        self.assertEqual(knight.get_possible_moves((0, 1), board), expected_moves)

    def test_knight_can_capture_enemy(self):
        board = Board()
        knight = Knight("WHITE")
        board.set_piece(0, 1, knight)  # Caballo blanco en su posición inicial en (0, 1)
        board.set_piece(2, 0, Knight("BLACK"))  # Caballo negro que puede ser capturado
        board.set_piece(2, 2, Knight("BLACK"))  # Caballo negro que puede ser capturado
        
        # Movimientos válidos donde el caballo blanco puede capturar
        expected_moves = [(2, 0), (2, 2)]
        self.assertEqual(knight.get_possible_moves((0, 1), board), expected_moves)


if __name__ == '__main__':
    unittest.main()
