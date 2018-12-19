class Board:
    def __init__(self):
        self._board = [" " for i in range(9)]

    def spaces(self):
        return self._board

    def space(self, cell):
        return self._board[cell-1] if self._board[cell-1] != " " else cell
        
    def make_move(self, input, player):
        self._board[input - 1] = player._symbol

    def is_full(self):
        return not " " in self._board
    
    def turn_count(self):
        return 9 - self._board.count(" ")
