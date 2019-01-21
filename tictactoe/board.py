from .constants import WINNING_COMBOS, EMPTY_SPACE

class Board:
    def __init__(self, board=None):
        self._board = [EMPTY_SPACE for i in range(9)] if board == None else board

    def spaces(self):
        return self._board

    def space(self, cell):
        return self._board[cell-1] if self._board[cell-1] != EMPTY_SPACE else cell

    def empty_cells(self):
        return [i for i, e in enumerate(self._board) if e == EMPTY_SPACE]

    def make_move(self, cell, player_symbol):
        self._board[cell-1] = player_symbol

    def turn_count(self):
        return 9 - self._board.count(EMPTY_SPACE)
