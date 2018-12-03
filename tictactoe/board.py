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
    
    def make_move(self, input, player):
        self._board[input - 1] = player._symbol
        return self._board
    
    def is_valid_move(self, input):
        return self._board[input - 1] == " "

    def is_full(self):
        return not " " in self._board
    
    def turn_count(self):
        return 9 - self._board.count(" ")
