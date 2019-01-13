import pickle
from sqlalchemy import MetaData, Table, desc, func, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from .create_database import SavedGame, BoardState, PlayerX, PlayerO
from tictactoe.ai_minimax import AIMinimax
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.validations import Validations
from tictactoe.board import Board
from tictactoe.cli_input import CLIInput
from tictactoe.cli_output import CLIOutput
from tictactoe.ui_wrapper import UIWrapper
import code

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

    def check_for_saved_game(self):
        session = self.create_session()
        saved_games = session.query(func.count(SavedGame.id)).filter(SavedGame.game_complete == False)
        return saved_games.scalar() > 0

    def retrieve_last_game(self):
        session = self.create_session()
        saved_game = session.query(SavedGame).filter(SavedGame.game_complete == False).order_by(desc(SavedGame.timestamp)).first()
        cli_input = CLIInput()
        ui = UIWrapper(CLIOutput())
        board_state = session.query(BoardState.state).filter(BoardState.saved_game_id == saved_game.id).first()
        board_obj = Board(board_state[0])
        player_x = session.query(PlayerX.id).filter(PlayerX.saved_game_id == saved_game.id).first()
        player_x_obj = Player("X", cli_input, ui)
        player_o = session.query(PlayerO.is_ai).filter(PlayerO.saved_game_id == saved_game.id).first()
        if player_o[0]:
            player_o_obj = AIMinimax("O")
        else:
            player_o_obj = Player("O", cli_input, ui)
        game_obj = Game(player_x_obj, player_o_obj, ui, Validations(), board_obj, saved_game.id)
        return game_obj
    
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
        session.commit()
        
    def add_game_to_database(self, game_object):
        session = self.create_session()
        board_list = game_object._board.spaces()
        board_state = BoardState(state=board_list)
        player_x = PlayerX()
        if type(game_object._player2) == AIMinimax:
            player_o = PlayerO(is_ai=True)
        else:
            player_o = PlayerO()

        current_game = SavedGame(board_state=[board_state], player_x=[player_x], player_o=[player_o])

        session.add(current_game)
        session.commit()

    def mark_complete_in_database(self, game_object):
        if game_object._id:
            self.update_game_in_database(game_object)
            session = self.create_session()
            completed_game = session.query(SavedGame).filter(SavedGame.id == game_object._id).first()
            completed_game.game_complete = True
            session.commit()