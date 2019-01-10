import datetime
from sqlalchemy import Column, Integer, PickleType, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    game = Column(PickleType)
    timestamp = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return "<Game(id='%s', game='%s', timestamp='%s')>" % (self.id, self.game, self.timestamp)