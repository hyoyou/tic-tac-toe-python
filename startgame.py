class StartGame:
    def start(self):
        print("Welcome to Tic Tac Toe")
        self.choose_game()
    
    def choose_game(self):
        print("""
        Please choose number of players (0-2):
        (0) Computer   v.   Computer
        (1) Player     v.   Computer
        (2) Player 1   v.   Player 2
        """)
        

game = StartGame()
game.start()