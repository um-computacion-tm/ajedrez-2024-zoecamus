import unittest
from .classboard import Board
from .movepawn import Pawn

class TestPawn(unittest.TestCase):
    
    def test_pawn_move_forward(self):
        board = Board()
        pawn = Pawn("WHITE")
        board.set_piece(6, 4, pawn)  
        expected_moves = [(5, 4), (4, 4)]  # Movimiento de 1 o 2 casillas hacia adelante
        self.assertEqual(pawn.get_possible_moves((6, 4), board), expected_moves)

    def test_pawn_move_capture(self):
        board = Board()
        pawn = Pawn("WHITE")
        board.set_piece(4, 4, pawn)  # Colocamos el peón blanco en (4, 4)
        board.set_piece(3, 3, Pawn("BLACK"))  # Colocamos un peón negro en la diagonal izquierda
        board.set_piece(3, 5, Pawn("BLACK"))  # Colocamos otro peón negro en la diagonal derecha
        
        expected_moves = [(3, 3), (3, 5)]  # Movimientos de captura en ambas diagonales
        self.assertEqual(pawn.get_possible_moves((4, 4), board), expected_moves)

    def test_pawn_blocked(self):
        board = Board()
        pawn = Pawn("WHITE")
        board.set_piece(4, 4, pawn)  # Colocamos el peón blanco en (4, 4)
        board.set_piece(3, 4, Pawn("BLACK"))  # Colocamos un peón negro bloqueando el avance en (3, 4)
        expected_moves = []  # No puede moverse hacia adelante
        self.assertEqual(pawn.get_possible_moves((4, 4), board), expected_moves)
    

if __name__ == '__main__':
    unittest.main()
 