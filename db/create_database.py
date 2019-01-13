import datetime
from sqlalchemy import Column, Integer, DateTime, String, Boolean, ForeignKey
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SavedGame(Base):
    __tablename__ = "saved_games"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.now)
    game_complete = Column(Boolean, default=False)
    board_state = relationship('BoardState', back_populates="saved_game")
    player_x = relationship('PlayerX', back_populates="saved_game")
    player_o = relationship('PlayerO', back_populates="saved_game")

    def __repr__(self):
        return "<Saved_Game(id='%s', game_complete='%s', timestamp='%s')>" % (self.id, self.game_complete, self.timestamp)

class BoardState(Base):
    __tablename__ = "board_states"

    id = Column(Integer, primary_key=True)
    state = Column(postgresql.ARRAY(String))
    saved_game_id = Column(Integer, ForeignKey('saved_games.id'))
    saved_game = relationship("SavedGame", back_populates="board_state", uselist=False)

    def __repr__(self):
        return "<BoardState(id='%s', saved_game_id='%s', state='%s')>" % (self.id, self.saved_game_id, self.state)

class PlayerX(Base):
    __tablename__ = "players_x"

    id = Column(Integer, primary_key=True)
    saved_game_id = Column(Integer, ForeignKey('saved_games.id'))
    saved_game = relationship("SavedGame", back_populates="player_x", uselist=False)

    def __repr__(self):
        return "<Player_X(id='%s', saved_game_id='%s')>" % (self.id, self.saved_game_id)

class PlayerO(Base):
    __tablename__ = "players_o"

    id = Column(Integer, primary_key=True)
    is_ai = Column(Boolean, default=False)
    saved_game_id = Column(Integer, ForeignKey('saved_games.id'))
    saved_game = relationship("SavedGame", back_populates="player_o", uselist=False)

    def __repr__(self):
        return "<Player_O(id='%s', saved_game_id='%s', is_ai='%s')>" % (self.id, self.saved_game_id, self.is_ai)