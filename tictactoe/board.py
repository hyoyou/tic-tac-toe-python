from tictactoe.constants import WINNING_COMBOS

class Board:
    def __init__(self):
        self._board = [" " for i in range(9)]

    def spaces(self):
        return self._board

    def space(self, cell):
        return self._board[cell-1] if self._board[cell-1] != " " else cell
        
    def make_move(self, cell, player):
        self._board[cell-1] = player._symbol

    def is_full(self):
        return not " " in self._board
    
    def is_winner(self):
        spaces = self.spaces()
        return any(spaces[combo[0]] == spaces[combo[1]] == spaces[combo[2]] and
               spaces[combo[0]] != " " for combo in WINNING_COMBOS)

    def turn_count(self):
        return 9 - self._board.count(" ")
