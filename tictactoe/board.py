from .constants import WINNING_COMBOS

class Board:
    def __init__(self, board=[" " for i in range(9)]):
        self._board = board

    def spaces(self):
        return self._board

    def space(self, cell):
        return self._board[cell-1] if self._board[cell-1] != " " else cell
    
    def empty_cells(self):
        return [i for i, e in enumerate(self._board) if e == " "]
        
    def make_move(self, cell, player_symbol):
        self._board[cell-1] = player_symbol

    def turn_count(self):
        return 9 - self._board.count(" ")
