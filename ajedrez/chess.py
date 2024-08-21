from chess import Chess

def main():
     chess = Chess()
     while True:
         play(Chess)

def play(Chess):
     try:
         from_row =  int(input('From row: '))
         from_col =  int(input('From column: '))
         to_row =  int(input('To row: '))
         to_col =  int(input('To column: '))

         Chess.move(from_row, from_col, to_row, to_col)

     except Exception as e:
         print('Invalid error')

                
if __name__ == '__main__':
    main()