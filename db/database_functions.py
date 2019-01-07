from sqlalchemy import MetaData, Table
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

# CRUD
# Create an entry
def add_game_to_database(game_object, session):
    engine.connect()
    new_game = Game(game=game_object)
    session.add(new_game)
    session.commit()
    # code.interact(local=locals())
    # <Game(id='3', game='<tictactoe.game.Game object at 0x106fb36a0>', timestamp='2019-01-04 13:26:51.719400')>
    session.close()

# Read an entry
def retrieve_last_game(session):
    connection = engine.connect()
    # SELECT id, game FROM games ORDER BY id DESC LIMIT 1;
    id, pickled_game, date = session.query(game).first()
    game_obj = pickle.loads(pickled_game)
    return game_obj
    # query = exists(query)

    return connection.execute(query)

# Update an entry
def update_game_database(game_object, session):
    pass
    # current_game = session.query(Games).last()
    # if current_game:
    #     current_game.game = game_object

# Destroy an entry