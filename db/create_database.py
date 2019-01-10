import datetime
from sqlalchemy import Column, Integer, DateTime, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    time_played = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return "<Game(id='%s', game='%s', time_played='%s')>" % (self.id, self.game, self.time_played)

class Board(Base):
    __tablename__ = "boards"

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    state = Column(String)

    def __repr__(self):
        return "<Game(id='%s', game_id='%s', state='%s')>" % (self.id, self.game_id, self.state)

class PlayerX(Base):
    __tablename__ = "players_x"

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))

    def __repr__(self):
        return "<Game(id='%s', game_id='%s')>" % (self.id, self.game_id)

class PlayerO(Base):
    __tablename__ = "players_o"

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('games.id'))
    is_ai = Column(Boolean, default=False)

    def __repr__(self):
        return "<Game(id='%s', game_id='%s', is_ai='%s')>" % (self.id, self.game_id, self.is_ai)