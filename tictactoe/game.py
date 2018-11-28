from tictactoe.player import Player
from tictactoe.board import Board

class Game:
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

    def __init__(self, player1 = Player("X"), player2 = Player("O"), board = Board()):
        self._player1 = player1
        self._player2 = player2
        self._board = board
    
    def current_player(self):
        turns = self._board.turn_count()
        if turns % 2 == 0:
            return self._player1
        else:
            return self._player2


game = Game()
print(game.current_player())