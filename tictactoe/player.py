class Player:
    def __init__(self, symbol, cli_input, cli_output):
        self._symbol = symbol
        self._input = cli_input
        self._output = cli_output

    def move(self, board):
        self._output.print_request_player_move(self._symbol)
        return self._input.get_input()