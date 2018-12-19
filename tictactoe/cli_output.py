class CLIOutput:
    def print(self, string):
        print(string)

    def print_board(self, board):
        print(f'''
         {board.space(1)} | {board.space(2)} | {board.space(3)} 
        ===+===+===
         {board.space(4)} | {board.space(5)} | {board.space(6)} 
        ===+===+===
         {board.space(7)} | {board.space(8)} | {board.space(9)} 
        ''')