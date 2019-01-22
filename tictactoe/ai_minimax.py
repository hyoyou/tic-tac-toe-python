from .constants import X, O, MIDDLE_CELL

class AIMinimax:
    def __init__(self, symbol, rules):
        self._symbol = symbol
        self._opponent = self.set_opponent_symbol(self._symbol)
        self._rules = rules

    def set_opponent_symbol(self, symbol):
        return O if symbol == X else X

    def move(self, board):
        if board.turn_count() == 0:
            return MIDDLE_CELL
        return self.minimax(board, self._symbol)[0]

    def minimax(self, board, player):
        available_moves = board.empty_cells()

        if self.is_terminal_state(board):
            return self.terminal_state_score(board)

        moves = []
        for i in available_moves:
            board.make_move(i+1, player)
            if player == self._symbol:
                score = self.minimax(board, self._opponent)[1]
                moves.append((i+1, score))
            elif player == self._opponent:
                score = self.minimax(board, self._symbol)[1]
                moves.append((i+1, score))
            board.make_move(i+1, " ")

        if player == self._opponent:
            return min(moves, key=lambda x: x[1])
        elif player == self._symbol:
            return max(moves, key=lambda x: x[1])

    def terminal_state_score(self, board):
        if self._rules.winning_symbol_check(self._opponent, board):
            return 0, -10
        elif self._rules.winning_symbol_check(self._symbol, board):
            return 0, 10
        return 0, 0

    def is_terminal_state(self, board):
        return self._rules.game_over(board)
