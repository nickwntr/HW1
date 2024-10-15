from fastapi import APIRouter
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.routers import *

from app.backend.db import Base

taskrouter = APIRouter(prefix="/user", tags=["user"])

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

@taskrouter.get("/")
async def all_tasks():
    pass

@taskrouter.get("/task_id")
async def task_by_id():
    pass

@taskrouter.post("/create")
async def create_task():
    pass

@taskrouter.put("/update")
async def update_task():
    pass

@taskrouter.delete("/delete")
async def delete_task():
    pass