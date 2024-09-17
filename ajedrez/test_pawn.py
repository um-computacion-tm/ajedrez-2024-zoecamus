import unittest
from .classboard import Board
from .movepawn import Pawn
from .classpieces import Pawn

class TestPawn(unittest.TestCase):
    
    def test_pawn_move_forward(self):
        board = Board()
        pawn = Pawn("WHITE")
        board.set_piece(6, 4, pawn)  
        expected_moves = [(5, 4), (4, 4)] 
        self.assertEqual(pawn.get_possible_moves((6, 4), board), expected_moves)

    def test_pawn_move_capture(self):
        board = Board()
        pawn = Pawn("WHITE")
        board.set_piece(4, 4, pawn)       
        board.set_piece(3, 3, Pawn("BLACK"))     
        board.set_piece(3, 5, Pawn("BLACK"))  


    def test_pawn_blocked(self):
        board = Board()
        pawn = Pawn("WHITE")
        board.set_piece(4, 4, pawn) 
        board.set_piece(3, 4, Pawn("BLACK"))  
        expected_moves = []  
        self.assertEqual(pawn.get_possible_moves((4, 4), board), expected_moves)

if __name__ == '__main__':
    unittest.main()