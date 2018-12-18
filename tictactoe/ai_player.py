import random
from tictactoe.game import Game
from tictactoe.validations import Validations

class AIPlayer:
    def __init__(self, symbol):
        self._symbol = symbol

    def move(self, board):
        validator = Validations()

        best_move = random.randint(1, 9)

        sym = self._symbol
        opp = "O" if sym == "X" else "X"

        if board.turn_count() == 0 and validator.is_valid_move(5, board._board):
            best_move = 5
        elif board.turn_count() == 1 and validator.is_valid_move(5, board._board):
            best_move = 5

        if board.turn_count() == 1 and validator.is_valid_move(3, board._board) and not validator.is_valid_move(5, board._board):
            best_move = 3
        elif board.turn_count() >= 2 and validator.is_valid_move(3, board._board):
            best_move = 3

        if board.turn_count() >= 2:
            for combo in Game.WINNING_COMBOS:
                if (board._board[combo[1]] == opp and 
                    board._board[combo[2]] == opp and
                    board._board[combo[0]] == " "):
                    best_move = combo[0] + 1
                elif (board._board[combo[0]] == opp and 
                    board._board[combo[2]] == opp and
                    board._board[combo[1]] == " "):
                    best_move = combo[1] + 1
                elif (board._board[combo[0]] == opp and 
                    board._board[combo[1]] == opp and
                    board._board[combo[2]] == " "):
                    best_move = combo[2] + 1

        if board.turn_count() >= 2:
            for combo in Game.WINNING_COMBOS:
                if (board._board[combo[1]] == sym and 
                    board._board[combo[2]] == sym and
                    board._board[combo[0]] == " "):
                    best_move = combo[0] + 1
                elif (board._board[combo[0]] == sym and 
                    board._board[combo[2]] == sym and
                    board._board[combo[1]] == " "):
                    best_move = combo[1] + 1
                elif (board._board[combo[0]] == sym and 
                    board._board[combo[1]] == sym and
                    board._board[combo[2]] == " "):
                    best_move = combo[2] + 1

        return best_move