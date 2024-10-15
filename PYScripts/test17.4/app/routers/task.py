from fastapi import APIRouter, Depends, status, HTTPException
from slugify import slugify
from typing import Annotated
from app.schemas import CreateTask, UpdateTask
from app.backend.db_depends import get_db
from app.modules.modules import *

from typing import Annotated

from app.routers import *

taskrouter = APIRouter(prefix="/task", tags=["task"])


@taskrouter.get("/")
async def all_tasks(get_db: Annotated[Session, Depends(get_db)]):
    tsks = get_db.scalars(select(Task)).all()
    return tsks

@taskrouter.get("/task_id")
async def task_by_id(get_db: Annotated[Session, Depends(get_db)], tsk_id: int):
    task = get_db.scalar(select(Task).where(tsk_id == Task.id))
    if task is None:
        raise HTTPException(404, "Task not found")
    return task
@taskrouter.post("/create")
async def create_task(get_db: Annotated[Session, Depends(get_db)],usr_id: int, newtask: CreateTask):
    usr = get_db.scalar(select(User).where(usr_id == User.id))
    if usr is None:
        raise HTTPException(404, "User not found")
    get_db.execute(insert(Task).values(
        title=newtask.title,
        content=newtask.content,
        priority=newtask.priority,
        user_id=usr_id
    ))
    get_db.commit()
    return {
        "status_code": status.HTTP_201_CREATED,
        "transaction": "success"
    }

@taskrouter.put("/update")
async def update_task(get_db: Annotated[Session, Depends(get_db)],tsk_id: int, updtask: UpdateTask):
    tsk = get_db.scalar(select(Task).where(tsk_id == Task.id))
    if tsk is None:
        raise HTTPException(404, "Task not found")
    get_db.execute(update(Task).where(tsk_id == Task.id).values(
        title=updtask.title,
        content=updtask.content,
        property=updtask.priority
    ))
    get_db.commit()
    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "Task updated"
    }

@taskrouter.delete("/delete")
async def delete_task(get_db: Annotated[Session, Depends(get_db)],tsk_id: int):
    tsk = get_db.scalar(select(Task).where(tsk_id == Task.id))
    if tsk is None:
        raise HTTPException(404, "Task not found")

    get_db.execute(delete(Task).where(tsk_id == Task.id))
    get_db.commit()
    return {
        "status_code": status.HTTP_200_OK,
        "transaction": "Task removed"
    }