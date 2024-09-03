from chess import Chess

def main():
     chess = Chess()
     while chess.is_playing():
         play(chess)

def play(Chess):
     try:
         print(Chess.show_board())
         print('Turn: ' + Chess.turn)
         from_row =  int(input('From row: '))
         from_col =  int(input('From column: '))
         to_row =  int(input('To row: '))
         to_col =  int(input('To column: '))

         Chess.move(from_row, from_col, to_row, to_col)

     except Exception as e:
         print('Invalid error')

                
@property
def turn(self):
        return self.__turn__

def show_board(self):
        return str(self.__board__)

def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
             self.__turn__ = "WHITE"
    
    
if __name__ == '__main__':
    main()