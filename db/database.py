from sqlalchemy import MetaData, Table, desc, func, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from .create_database import SavedGame, BoardState, PlayerX, PlayerO
from tictactoe.ai_minimax import AIMinimax
from tictactoe.board import Board
from tictactoe.cli_input import CLIInput
from tictactoe.cli_output import CLIOutput
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.rules import Rules
from tictactoe.ui_wrapper import UIWrapper
from tictactoe.validations import Validations

class Database:
    def __init__(self, engine):
        self.engine = engine
        self.find_or_create_tables(self.engine)

    def find_or_create_tables(self, engine):
        SavedGame.__table__.create(engine, checkfirst=True)
        BoardState.__table__.create(engine, checkfirst=True)
        PlayerX.__table__.create(engine, checkfirst=True)
        PlayerO.__table__.create(engine, checkfirst=True)

    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def check_for_in_progress_game(self):
        session = self.create_session()
        saved_games = session.query(func.count(SavedGame.id)).filter(SavedGame.game_complete == False)
        return saved_games.scalar() > 0

    def retrieve_last_game(self):
        session = self.create_session()
        saved_game = session.query(SavedGame).filter(SavedGame.game_complete == False).order_by(desc(SavedGame.timestamp)).first()
        return self.recreate_game_object(saved_game)

    def recreate_game_object(self, saved_game):
        cli_input = CLIInput()
        ui = UIWrapper(CLIOutput())
        board_obj = self.create_board_object(saved_game)
        player_x_obj = self.create_player_x_object(saved_game, cli_input, ui)
        player_o_obj = self.create_player_o_object(saved_game, cli_input, ui)

        game_obj = Game(player_x_obj, player_o_obj, ui, Validations(), Rules(), board_obj, saved_game.id)
        return game_obj

    def create_board_object(self, saved_game):
        session = self.create_session()
        board_state = session.query(BoardState.state).filter(BoardState.saved_game_id == saved_game.id).first()
        return Board(board_state[0])

    def create_player_x_object(self, saved_game, cli_input, ui):
        session = self.create_session()
        player_x = session.query(PlayerX.is_ai).filter(PlayerX.saved_game_id == saved_game.id).first()
        if player_x[0]:
            return AIMinimax("X", Rules())
        else:
            return Player("X", cli_input, ui)

    def create_player_o_object(self, saved_game, cli_input, ui):
        session = self.create_session()
        player_o = session.query(PlayerO.is_ai).filter(PlayerO.saved_game_id == saved_game.id).first()
        if player_o[0]:
            return AIMinimax("O", Rules())
        else:
            return Player("O", cli_input, ui)

    def add_or_update_database(self, game_object):
        if game_object._id:
            self.update_game_in_database(game_object)
        else:
            self.add_game_to_database(game_object)

    def update_game_in_database(self, game_object):
        conn = self.engine.connect()
        session = self.create_session()
        in_progress_game = session.query(SavedGame).filter(SavedGame.id == game_object._id).first()
        updated_board = update(BoardState).where(BoardState.saved_game_id == in_progress_game.id).values(state=game_object._board.spaces())
        conn.execute(updated_board)
        conn.close()

    def add_game_to_database(self, game_object):
        session = self.create_session()
        board_state = self.add_board_entry_to_database(game_object)
        player_x = self.add_player_x_entry_to_database(game_object)
        player_o = self.add_player_o_entry_to_database(game_object)

        current_game = SavedGame(board_state=[board_state], player_x=[player_x], player_o=[player_o])
        session.add(current_game)
        session.commit()

    def add_board_entry_to_database(self, game_object):
        board_list = game_object._board.spaces()
        return BoardState(state=board_list)

    def add_player_x_entry_to_database(self, game_object):
        if type(game_object._player1) == AIMinimax:
            return PlayerX(is_ai=True)
        else:
            return PlayerX()

    def add_player_o_entry_to_database(self, game_object):
        if type(game_object._player2) == AIMinimax:
            return PlayerO(is_ai=True)
        else:
            return PlayerO()

    def mark_complete_in_database(self, game_object):
        if game_object._id:
            self.update_game_in_database(game_object)
            session = self.create_session()
            completed_game = session.query(SavedGame).filter(SavedGame.id == game_object._id).first()
            completed_game.game_complete = True
            session.commit()
