class Board:
    def __init__(self, cli_output):
        self._board = [" " for i in range(9)]
        self._output = cli_output
    
    def display_board(self):
        self._output.print(f'''
         {self._board[0] if self._board[0] != " " else 1} | {self._board[1] if self._board[1] != " " else 2} | {self._board[2] if self._board[2] != " " else 3} 
        ===+===+===
         {self._board[3] if self._board[3] != " " else 4} | {self._board[4] if self._board[4] != " " else 5} | {self._board[5] if self._board[5] != " " else 6} 
        ===+===+===
         {self._board[6] if self._board[6] != " " else 7} | {self._board[7] if self._board[7] != " " else 8} | {self._board[8] if self._board[8] != " " else 9} 
        ''')
    
    def make_move(self, input, player):
        self._board[input - 1] = player._symbol
    
    def is_valid_move(self, input):
        if input >= 1 and input <= 9:
            return self._board[input - 1] == " "
        else:
            return False

    def is_full(self):
        return not " " in self._board
    
    def turn_count(self):
        return 9 - self._board.count(" ")
