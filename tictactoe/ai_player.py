import random
from tictactoe.game import Game
from tictactoe.validations import Validations

class AIPlayer:
    def __init__(self, symbol):
        self._symbol = symbol

    def move(self, board):
        validator = Validations()
        spaces = board.spaces()
        best_move = random.randint(1, 9)

        sym = self._symbol
        opp = "O" if sym == "X" else "X"

        if board.turn_count() == 0 and validator.is_valid_move(5, spaces):
            best_move = 5
        elif board.turn_count() == 1 and validator.is_valid_move(5, spaces):
            best_move = 5

        if board.turn_count() == 1 and validator.is_valid_move(3, spaces) and not validator.is_valid_move(5, spaces):
            best_move = 3
        elif board.turn_count() >= 2 and validator.is_valid_move(3, spaces):
            best_move = 3

        if board.turn_count() >= 2:
            for combo in Game.WINNING_COMBOS:
                if (spaces[combo[1]] == opp and 
                    spaces[combo[2]] == opp and
                    spaces[combo[0]] == " "):
                    best_move = combo[0] + 1
                elif (spaces[combo[0]] == opp and 
                    spaces[combo[2]] == opp and
                    spaces[combo[1]] == " "):
                    best_move = combo[1] + 1
                elif (spaces[combo[0]] == opp and 
                    spaces[combo[1]] == opp and
                    spaces[combo[2]] == " "):
                    best_move = combo[2] + 1

        if board.turn_count() >= 2:
            for combo in Game.WINNING_COMBOS:
                if (spaces[combo[1]] == sym and 
                    spaces[combo[2]] == sym and
                    spaces[combo[0]] == " "):
                    best_move = combo[0] + 1
                elif (spaces[combo[0]] == sym and 
                    spaces[combo[2]] == sym and
                    spaces[combo[1]] == " "):
                    best_move = combo[1] + 1
                elif (spaces[combo[0]] == sym and 
                    spaces[combo[1]] == sym and
                    spaces[combo[2]] == " "):
                    best_move = combo[2] + 1

        return best_move