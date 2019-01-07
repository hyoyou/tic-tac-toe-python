import datetime
from sqlalchemy import *
from sqlalchemy.sql import *
from sqlalchemy.ext.declarative import declarative_base
from db import engine

Base = declarative_base()

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    game = Column(PickleType)
    timestamp = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return "<Game(id='%s', game='%s', timestamp='%s')>" % (self.id, self.game, self.timestamp)

Game.__table__.create(bind=engine, checkfirst=True)