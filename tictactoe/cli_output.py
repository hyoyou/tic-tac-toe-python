class CLIOutput:
    def print(self, string):
        print(string)

    def print_board(self, board):
        print(f'''
         {board[0] if board[0] != " " else 1} | {board[1] if board[1] != " " else 2} | {board[2] if board[2] != " " else 3} 
        ===+===+===
         {board[3] if board[3] != " " else 4} | {board[4] if board[4] != " " else 5} | {board[5] if board[5] != " " else 6} 
        ===+===+===
         {board[6] if board[6] != " " else 7} | {board[7] if board[7] != " " else 8} | {board[8] if board[8] != " " else 9} 
        ''')