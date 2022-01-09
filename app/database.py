from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

engine = create_engine("postgresql://postgres:postgres@localhost/forum_db", echo=False)

Base = declarative_base()

session = scoped_session(sessionmaker(engine))