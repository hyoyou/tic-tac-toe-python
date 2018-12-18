class Board:
    def __init__(self, cli_output):
        self._board = [" " for i in range(9)]
        # self._output = cli_output
    
    # def display_board(self):
    #     self._output.print_board(self._board)
    
    def make_move(self, input, player):
        self._board[input - 1] = player._symbol
    
    # def is_valid_move(self, input):
    #     if input >= 1 and input <= 9:
    #         return self._board[input - 1] == " "
    #     else:
    #         return False

    def is_full(self):
        return not " " in self._board
    
    def turn_count(self):
        return 9 - self._board.count(" ")
