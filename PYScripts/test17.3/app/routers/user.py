from fastapi import APIRouter
from app.backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.routers import *

userrouter = APIRouter(prefix="/task", tags=["task"])

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    frstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship("Task",back_populates="user")

@userrouter.get("/")
async def all_users():
    pass

@userrouter.get("/user_id")
async def user_by_id():
    pass

@userrouter.post("/create")
async def create_user():
    pass

@userrouter.put("/update")
async def update_user():
    pass

@userrouter.delete("/delete")
async def delete_user():
    pass