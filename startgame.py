from sqlalchemy import create_engine
from db.database import Database
from tictactoe.cli_input import CLIInput
from tictactoe.cli_output import CLIOutput
from tictactoe.setup_game import SetupGame
from settings import DB_ADDRESS

class StartGame:
    def __init__(self, setup_game):
        self.setup_game = setup_game

    def run(self):
        new_game = self.setup_game.run()
        new_game.game_play_loop(self.setup_game._db)

if __name__ == '__main__':
    engine = create_engine(DB_ADDRESS)
    setup_game = SetupGame(CLIInput(), CLIOutput(), engine)
    StartGame(setup_game).run()
