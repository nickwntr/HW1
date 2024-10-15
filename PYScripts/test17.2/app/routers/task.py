from fastapi import APIRouter
from app.backend.db import Base

taskrouter = APIRouter(prefix="/user", tags=["user"])

class Task(Base):
    __tablename__ = 'tasks'

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