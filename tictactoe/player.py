class Player:
    def __init__(self, symbol, input_getter):
        self._input = input_getter
        self._symbol = symbol

    def move(self, board):
        return self._input.get_input("Please make a move: ")
        
