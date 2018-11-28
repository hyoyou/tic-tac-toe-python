class Player:
    def __init__(self, symbol):
        self._symbol = symbol

    def move(self, board):
        player_move = input("Please make a move: ")
