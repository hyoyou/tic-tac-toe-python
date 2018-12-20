import random
from tictactoe.game import Game
from tictactoe.validations import Validations

class AIPlayer:
    def __init__(self, symbol):
        self._symbol = symbol

    def move(self, board):
        validator = Validations()
        
        sym = self._symbol
        opp = "O" if sym == "X" else "X"

        if validator.is_empty(5, board):
            return 5

        if validator.is_empty(3, board):
            return 3
   
        if self.make_move(board, sym) != None:
            return self.make_move(board, sym)
        elif self.make_move(board, opp) != None:
            return self.make_move(board, opp)
        
        return self.random_move(board, validator)
        
    def make_move(self, board, sym):
        spaces = board.spaces()

        for combo in Game.WINNING_COMBOS:
            if (spaces[combo[1]] == sym and 
                spaces[combo[2]] == sym and
                spaces[combo[0]] == " "):
                return combo[0] + 1
            elif (spaces[combo[0]] == sym and 
                spaces[combo[2]] == sym and
                spaces[combo[1]] == " "):
                return combo[1] + 1
            elif (spaces[combo[0]] == sym and 
                spaces[combo[1]] == sym and
                spaces[combo[2]] == " "):
                return combo[2] + 1
        
        return None

    def random_move(self, board, validator):
        best_move = 5
        while not validator.is_empty(best_move, board):
            best_move = random.randint(1, 9)

        return best_move