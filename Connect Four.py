Rows = 6
Columns = 7 
Empty = '.'
First_player = 'X'
Second_player = 'O'

def create_board():
    return [[Empty for _ in range(Columns)] for _ in range(Rows)]
