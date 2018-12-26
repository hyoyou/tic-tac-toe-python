import random
from tictactoe.game import Game
from tictactoe.validations import Validations
from tictactoe.constants import *

class AIPlayer:
    def __init__(self, symbol):
        self._symbol = symbol

    def move(self, board):
        validator = Validations()
        
        sym = self._symbol
        opp = O if sym == X else X

        if self.middle_cell_is_available(validator, board):
            return MIDDLE_CELL

        if self.corner_cell_is_available(validator, board):
            return CORNER_CELL
   
        if self.winning_move_is_available(board, sym):
            return self.make_move(board, sym)
        elif self.opponent_block_is_needed(board, opp):
            return self.make_move(board, opp)
        
        return self.random_move(board, validator)
        
    def middle_cell_is_available(self, validator, board):
        return validator.is_empty(5, board)
    
    def corner_cell_is_available(self, validator, board):
        return validator.is_empty(3, board)
    
    def winning_move_is_available(self, board, symbol):
        return self.make_move(board, symbol) != None
    
    def opponent_block_is_needed(self, board, symbol):
        return self.make_move(board, symbol) != None

    def make_move(self, board, symbol):
        spaces = board.spaces()
        for combo in WINNING_COMBOS:
            if (spaces[combo[1]] == symbol and 
                spaces[combo[2]] == symbol and
                spaces[combo[0]] == " "):
                return combo[0] + 1
            elif (spaces[combo[0]] == symbol and 
                spaces[combo[2]] == symbol and
                spaces[combo[1]] == " "):
                return combo[1] + 1
            elif (spaces[combo[0]] == symbol and 
                spaces[combo[1]] == symbol and
                spaces[combo[2]] == " "):
                return combo[2] + 1
        return None

    def random_move(self, board, validator):
        best_move = 5
        while not validator.is_empty(best_move, board):
            best_move = random.randint(1, 9)
        return best_move