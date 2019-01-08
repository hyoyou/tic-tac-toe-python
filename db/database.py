import pickle
from sqlalchemy import MetaData, Table, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from .create_database import Game

class Database:
    def __init__(self, engine):
        self.engine = engine
        Game.__table__.create(engine, checkfirst=True)
        self.meta = MetaData(bind=self.engine)
        self.game = Table("games", self.meta, autoload=True, autoload_with=self.engine)

    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def check_for_saved_game(self):
        session = self.create_session()
        saved_game = session.query(self.game).count()
        session.close()
        return saved_game > 0

    def retrieve_last_game(self):
        session = self.create_session()
        game_id, pickled_game, date = session.query(self.game).order_by(desc(Game.id)).first()
        game_obj = pickle.loads(pickled_game)
        return game_obj

    def add_game_to_database(self, game_object):
        session = self.create_session()
        if self.check_for_saved_game():
            self.delete_game_from_database()
        current_game = Game(game=game_object)
        session.add(current_game)
        session.commit()
        session.close()

    def delete_game_from_database(self):
        session = self.create_session()
        if session.query(self.game).order_by(desc(Game.id)).first():
            completed_game_id, pickled_game, date = session.query(self.game).order_by(desc(Game.id)).first()
            completed_game_entry = session.query(Game).filter_by(id = completed_game_id).one()
            session.delete(completed_game_entry)
            session.commit()
            session.close()