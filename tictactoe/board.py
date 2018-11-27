class Board:
    def __init__(self):
        self.board = [" " for i in range(9)]
    
    def display_board(self):
        return self.board