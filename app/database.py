from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

engine = create_engine("postgresql://postgres:postgres@localhost/forum_db", echo=False)

session = scoped_session(sessionmaker(engine))

Base = declarative_base()
