class Board:
    def __init__(self):
        self._board = [" " for i in range(9)]
    
    def display_board(self):
        return f'''
         {self._board[0]} | {self._board[1]} | {self._board[2]} 
        ===+===+===
         {self._board[3]} | {self._board[4]} | {self._board[5]} 
        ===+===+===
         {self._board[6]} | {self._board[7]} | {self._board[8]} 
        '''
    
    def make_move(self, input):
        self._board[input - 1] = "X"
        return self._board

test = Board()
print(test.display_board())