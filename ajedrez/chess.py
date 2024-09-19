from .classchess import Chess

def main():
     chess = Chess()
     while chess.is_playing():
         play(chess)

def play(chess_instance):
    try:
        print(chess_instance.show_board())
        print('Turn: ' + chess_instance.turn)
        
        from_row = int(input('From row: '))
        from_col = int(input('From column: '))
        to_row = int(input('To row: '))
        to_col = int(input('To column: '))
        
        chess_instance.move(from_row, from_col, to_row, to_col)
    
        chess_instance.change_turn()

    except Exception as e:
        print(f'Invalid move: {e}')

if __name__ == '__main__':
    main()