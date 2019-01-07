from sqlalchemy import MetaData, Table, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from sqlalchemy.sql.expression import exists
from .create_database import Game
import code
import pickle
from db import engine

meta = MetaData(bind=engine)
game = Table("games", meta, autoload=True, autoload_with=engine)

def create_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def check_for_saved_game():
    session = create_session()
    saved_game = session.query(game).count()
    return saved_game > 0

def retrieve_last_game(session):
    engine.connect()
    game_id, pickled_game, date = session.query(game).order_by(desc(Game.id)).first()
    game_obj = pickle.loads(pickled_game)
    return game_obj

def add_game_to_database(game_object, session):
    engine.connect()
    current_game = Game(game=game_object)
    session.add(current_game)
    session.commit()
    session.close()

def delete_game_from_database(session):
    engine.connect()
    if session.query(game).order_by(desc(Game.id)).first():
        completed_game_id, pickled_game, date = session.query(game).order_by(desc(Game.id)).first()
        completed_game_entry = session.query(Game).filter_by(id = completed_game_id).one()
        session.delete(completed_game_entry)
        session.commit()
        session.close()