from tictactoe.cli_input import CLIInput
from tictactoe.cli_output import CLIOutput
from tictactoe.setup_game import SetupGame

class StartGame:
    def __init__(self, setup_game):
        self.setup_game = setup_game

    def run(self):
        new_game = self.setup_game.run()
        new_game.game_play_loop()

if __name__ == '__main__':
    setup_game = SetupGame(CLIInput(), CLIOutput())
    StartGame(setup_game).run()
