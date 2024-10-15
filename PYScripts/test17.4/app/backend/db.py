import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column,Row,Integer,String

engine = create_engine("sqlite:///taskmanager.db")

currSession = sessionmaker(bind=engine)
class Base(DeclarativeBase):
    pass
