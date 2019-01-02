from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import *

engine = create_engine('postgresql:///game.db')

Base = declarative_base()

class Games(Base):
    __tablename__ = "games"
    GameId = Column(Integer, primary_key=True)
    XPlayerId = Column(Integer)
    OPlayerId = Column(Integer)
    BoardId = Column(Integer)
    Timestamp = Column(DateTime)

class XPlayer(Base):
    __tablename__ = "x_player_id"