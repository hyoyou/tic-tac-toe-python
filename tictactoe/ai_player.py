import random

class AIPlayer:
    def __init__(self, symbol):
        self._symbol = symbol

    def move(self, board):
        best_move = random.randint(1, 11)

        # Try to take the center
        if board.turn_count() == 0 and board.is_valid_move(5):
            best_move = 5
        elif board.turn_count() == 1 and board.is_valid_move(5):
            best_move = 5

        # Try to take the corner
        if board.turn_count() == 1 and board.is_valid_move(3) and not board.is_valid_move(5):
            best_move = 3
        elif board.turn_count() >= 2 and board.is_valid_move(3):
            best_move = 3


        return best_move