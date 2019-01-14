from .constants import X, O
from .rules import Rules

class AIMinimax:
    def __init__(self, symbol):
        self._symbol = symbol
        self._rules = Rules()

    def move(self, board):
        return self.minimax(board, O)[0]

    def minimax(self, board, player):
        available_moves = board.empty_cells()

        if self.is_terminal_state(board):     
            for player in [O, X]:
                return self.terminal_state_score(board, player)

        moves = []
        for i in available_moves:
            board.make_move(i+1, player)
            if player == O:
                score = self.minimax(board, X)[1]
                moves.append((i+1, score))
            elif player == X:
                score = self.minimax(board, O)[1]
                moves.append((i+1, score))
            board.make_move(i+1, " ")

        if player == X:
            return min(moves, key=lambda x: x[1])
        elif player == O:
            return max(moves, key=lambda x: x[1])

    def terminal_state_score(self, board, player):
        if self._rules.winning_symbol_check(X, board):
            return 0, -10
        elif self._rules.winning_symbol_check(O, board):
            return 0, 10
        return 0, 0

    def is_terminal_state(self, board):
        return self._rules.game_over(board)