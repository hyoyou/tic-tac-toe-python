from .constants import WINNING_COMBOS
from .ui_wrapper import UIWrapper

class Rules:
    def is_winner(self, board):
        spaces = board.spaces()
        return any(spaces[combo[0]] == spaces[combo[1]] == spaces[combo[2]] and
               spaces[combo[0]] != " " for combo in WINNING_COMBOS)

    def is_full(self, board):
        return not " " in board.spaces()

    def game_over(self, board):
        return self.is_winner(board) or self.is_full(board)

    def winner(self, board):
        for combo in WINNING_COMBOS:
            if self.match_symbol(combo, board):
                return self.match_symbol(combo, board)

    def match_symbol(self, combo, board):
        spaces = board.spaces()
        if spaces[combo[0]] == spaces[combo[1]] == spaces[combo[2]] and spaces[combo[0]] != " ":
            return spaces[combo[0]]

    def winning_symbol_check(self, symbol, board):
        for combo in WINNING_COMBOS:
            if self.is_matching_symbol(board, combo, symbol):
                return self.is_matching_symbol(board, combo, symbol)

    def is_matching_symbol(self, board, combo, symbol):
        spaces = board.spaces()
        return spaces[combo[0]] == spaces[combo[1]] == spaces[combo[2]] and spaces[combo[0]] == symbol

