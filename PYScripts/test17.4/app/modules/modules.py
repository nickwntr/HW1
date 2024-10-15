from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, insert, select, update, delete
from sqlalchemy.orm import relationship, Session
from app.backend.db import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True,index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean,default=False)
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False,index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship("User",back_populates="tasks")


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    frstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship("Task",back_populates="user")