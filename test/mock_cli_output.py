class MockCLIOutput:
    def __init__(self):
        self._last_output = ""

    def print(self, string):
        self._last_output += string

    def print_board(self, board):
        self._display_board = (f'''
         {board.space(1)} | {board.space(2)} | {board.space(3)} 
        ===+===+===
         {board.space(4)} | {board.space(5)} | {board.space(6)} 
        ===+===+===
         {board.space(7)} | {board.space(8)} | {board.space(9)} 
        ''')
