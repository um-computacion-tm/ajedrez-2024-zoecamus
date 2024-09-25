import unittest
from .classboard import Board
from .moveknight import Knight

class TestKnight(unittest.TestCase):
    
    def test_knight_initial_position_white(self):
        board = Board()
        knight = Knight("WHITE")
        board.set_piece(0, 1, knight)  
        
       
        expected_moves = [(2, 0), (2, 2)]
        self.assertEqual(knight.get_possible_moves((0, 1), board), expected_moves)

    def test_knight_initial_position_black(self):
        board = Board()
        knight = Knight("BLACK")
        board.set_piece(7, 1, knight)  
        
        
        expected_moves = [(5, 0), (5, 2)]
        self.assertEqual(knight.get_possible_moves((7, 1), board), expected_moves)

    def test_knight_blocked_by_own_pieces(self):
        board = Board()
        knight = Knight("WHITE")
        board.set_piece(0, 1, knight)  
        board.set_piece(2, 0, Knight("WHITE"))  
        board.set_piece(2, 2, Knight("WHITE"))  
        
       
        expected_moves = []
        self.assertEqual(knight.get_possible_moves((0, 1), board), expected_moves)

    def test_knight_can_capture_enemy(self):
        board = Board()
        knight = Knight("WHITE")
        board.set_piece(0, 1, knight) 
        board.set_piece(2, 0, Knight("BLACK"))  
        board.set_piece(2, 2, Knight("BLACK")) 
       

        expected_moves = [(2, 0), (2, 2)]
        self.assertEqual(knight.get_possible_moves((0, 1), board), expected_moves)


if __name__ == '__main__':
    unittest.main()
