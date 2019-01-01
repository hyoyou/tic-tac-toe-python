import code
from operator import itemgetter
from tictactoe.constants import *

class AIMinimax:
    def __init__(self, symbol):
        self._symbol = symbol

    def move(self, board):
        return self.minimax(board, O)[0]

    def minimax(self, board, player):
        available_moves = board.empty_cells()

        if self.is_terminal_state(board):     
            for player in [O, X]:
                return self.terminal_state_score(board, player)

        moves = []

        for i in available_moves:
            board._board[i] = player

            if player == O:
                score = self.minimax(board, X)[1]
                moves.append((i+1, score))
            elif player == X:
                score = self.minimax(board, O)[1]
                moves.append((i+1, score))

            board._board[i] = " "

        if player == X:
            return min(moves, key=itemgetter(1))
        elif player == O:
            return max(moves, key=itemgetter(1))

    def winning_player(self, board, player):
        if (board._board[0] == player and board._board[1] == player and board._board[2] == player or
            board._board[3] == player and board._board[4] == player and board._board[5] == player or
            board._board[6] == player and board._board[7] == player and board._board[8] == player or
            board._board[0] == player and board._board[3] == player and board._board[6] == player or
            board._board[1] == player and board._board[4] == player and board._board[7] == player or
            board._board[2] == player and board._board[5] == player and board._board[8] == player or
            board._board[0] == player and board._board[4] == player and board._board[8] == player or
            board._board[2] == player and board._board[4] == player and board._board[6] == player):
            return True
        else:
            return False

    def terminal_state_score(self, board, player):
        if self.winning_player(board, X):
            return 0, -10
        elif self.winning_player(board, O):
            return 0, 10
        return 0, 0

    def is_terminal_state(self, board):
        return board.game_over()