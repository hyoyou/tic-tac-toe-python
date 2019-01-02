from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://heatheryou:hello@localhost:5432/tictactoe')
# meta = MetaData(bind=engine)
# game = Table("games", meta, autoload=True, autoload_with=engine)