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


    def test_str_white_rook(self):
        board = Board()
        rook = Rook("WHITE")
        self.assertEqual(str(rook), "♜")

    def test_str_black_rook(self):
        board = Board()
        rook = Rook("BLACK")
        self.assertEqual(str(rook), "♖")



    def test_rook_move_vertical(self):
        board = Board()
        rook = Rook("WHITE")
        board.set_piece(4, 4, rook)
        expected_moves = [(5, 4), (6, 4), (7, 4), (3, 4), (2, 4), (1, 4), (0, 4)]
        self.assertEqual(set(rook.get_possible_moves((4, 4), board)), set(expected_moves))

    def test_rook_move_horizontal(self):
        board = Board()
        rook = Rook("WHITE")
        board.set_piece(4, 4, rook)
        expected_moves = [(4, 5), (4, 6), (4, 7), (4, 3), (4, 2), (4, 1), (4, 0)]
        self.assertEqual(set(rook.get_possible_moves((4, 4), board)), set(expected_moves))

    def test_rook_move_with_obstacle(self):
        board = Board()
        rook = Rook("WHITE")
        board.set_piece(4, 4, rook)
        board.set_piece(5, 4, Pawn("BLACK"))  # Obstacle in the vertical path
        expected_moves = [(5, 4), (6, 4), (7, 4), (3, 4), (2, 4), (1, 4), (0, 4), (4, 5), (4, 6), (4, 7), (4, 3), (4, 2), (4, 1), (4, 0)]
        self.assertEqual(set(rook.get_possible_moves((4, 4), board)), set(expected_moves))

    def test_rook_move_with_friendly_piece(self):
        board = Board()
        rook = Rook("WHITE")
        board.set_piece(4, 4, rook)
        board.set_piece(5, 4, Pawn("WHITE"))  # Friendly piece in the vertical path
        expected_moves = [(6, 4), (7, 4), (3, 4), (2, 4), (1, 4), (0, 4), (4, 5), (4, 6), (4, 7), (4, 3), (4, 2), (4, 1), (4, 0)]
        self.assertEqual(set(rook.get_possible_moves((4, 4), board)), set(expected_moves))

    def test_rook_move_with_enemy_piece(self):
        board = Board()  # Asegúrate de que Board se inicializa correctamente
        rook = Rook("WHITE")
        board.set_piece(4, 4, rook)
        board.set_piece(5, 4, Pawn("BLACK"))  # Enemy piece
        expected_moves = [(5, 4), (6, 4), (7, 4), (3, 4), (2, 4), (1, 4), (0, 4), (4, 5), (4, 6), (4, 7), (4, 3), (4, 2), (4, 1), (4, 0)]
        self.assertEqual(set(rook.get_possible_moves((4, 4), board)), set(expected_moves))


    def test_rook_on_edge(self):
        board = Board()
        rook = Rook("WHITE")
        board.set_piece(0, 0, rook)
        expected_moves = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
        self.assertEqual(set(rook.get_possible_moves((0, 0), board)), set(expected_moves))

























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