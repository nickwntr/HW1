from fastapi import APIRouter
from app.backend.db import Base

userrouter = APIRouter(prefix="/task", tags=["task"])

class Task(Base):
    __tablename__ = 'users'

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