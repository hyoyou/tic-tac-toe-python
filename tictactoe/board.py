from .constants import WINNING_COMBOS

class Board:
    def __init__(self):
        self._board = [" " for i in range(9)]

    def spaces(self):
        return self._board

    def space(self, cell):
        return self._board[cell-1] if self._board[cell-1] != " " else cell
    
    def empty_cells(self):
        return [i for i, e in enumerate(self._board) if e == " "]
        
    def make_move(self, cell, player_symbol):
        self._board[cell-1] = player_symbol

    def is_full(self):
        return not " " in self._board
    
    def is_winner(self):
        spaces = self.spaces()
        return any(spaces[combo[0]] == spaces[combo[1]] == spaces[combo[2]] and
               spaces[combo[0]] != " " for combo in WINNING_COMBOS)

    def winning_symbol_check(self, symbol):
        for combo in WINNING_COMBOS:
            if self.is_matching_symbol(combo, symbol):
                return self.is_matching_symbol(combo, symbol)
    
    def is_matching_symbol(self, combo, symbol):
        spaces = self.spaces()
        return spaces[combo[0]] == spaces[combo[1]] == spaces[combo[2]] and spaces[combo[0]] == symbol

    def game_over(self):
        return self.is_winner() or self.is_full()

    def turn_count(self):
        return 9 - self._board.count(" ")
