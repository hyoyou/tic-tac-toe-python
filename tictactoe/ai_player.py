import random

class AIPlayer:
    WINNING_COMBOS = [
        [0, 1, 2], # Top row
        [3, 4, 5], # Middle row
        [6, 7, 8], # Bottom row
        [0, 3, 6], # Left column
        [1, 4, 7], # Middle column
        [2, 5, 8], # Right column
        [0, 4, 8], # Left diagonal
        [2, 4, 6]  # Right diagonal
    ]

    def __init__(self, symbol):
        self._symbol = symbol

    def move(self, board):
        best_move = random.randint(1, 9)

        sym = self._symbol
        opp = "O" if sym == "X" else "X"

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

        # Best moves after first 2 moves made:
        # Move for a block
        if board.turn_count() >= 2:
            for combo in self.WINNING_COMBOS:
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

        # Move for a win
        if board.turn_count() >= 2:
            for combo in self.WINNING_COMBOS:
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