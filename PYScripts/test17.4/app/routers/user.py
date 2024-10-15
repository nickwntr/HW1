from fastapi import APIRouter, Depends, status, HTTPException
from slugify import slugify
from typing import Annotated
from app.schemas import CreateUser, UpdateUser
from app.backend.db_depends import get_db
from app.modules.modules import *

userrouter = APIRouter(prefix="/user", tags=["user"])


@userrouter.get("/")
async def all_users(get_db: Annotated[Session, Depends(get_db)]):
    usrs = get_db.scalars(select(User)).all()
    return usrs


@userrouter.get("/user_id")
async def user_by_id(get_db: Annotated[Session, Depends(get_db)],usr_id : int):
    usr = get_db.scalar(select(User).where(usr_id == User.id))
    if usr is None:
        raise HTTPException(404,"User not found")
    return usr

@userrouter.get("/{usr_id}/tasks")
async def tasks_by_user_id(get_db: Annotated[Session, Depends(get_db)],usr_id : int):
    tsks = get_db.scalars(select(Task).where(usr_id == Task.user_id)).all()
    return tsks

@userrouter.post("/create")
async def create_user(get_db: Annotated[Session, Depends(get_db)],newuser : CreateUser):
    get_db.execute(insert(User).values(username=newuser.username,
                                       frstname=newuser.frstname,
                                       lastname=newuser.lastname,
                                       age=newuser.age,
                                       slug = slugify(newuser.username)))
    get_db.commit()

    return {
        "status_code": status.HTTP_201_CREATED,
        "transaction": "success"
    }

@userrouter.put("/update")
async def update_user(get_db: Annotated[Session, Depends(get_db)],upduser : UpdateUser,usr_id:int):
    usr = get_db.scalar(select(User).where(usr_id == User.id))
    if usr is None:
        raise HTTPException(404, "User not found")

    get_db.execute(update(User).where(usr_id == User.id).values(
        frstname=upduser.frstname,
        lastname=upduser.lastname,
        age=upduser.age
    ))
    get_db.commit()
    return {
        "status_code":status.HTTP_200_OK,
        "transaction": f"User {usr_id} updated"
    }


@userrouter.delete("/delete")
async def delete_user(get_db: Annotated[Session, Depends(get_db)],usr_id:int):
    usr = get_db.scalar(select(User).where(usr_id == User.id))
    if usr is None:
        raise HTTPException(404, "User not found")

    get_db.execute(delete(Task).where(Task.user_id == usr_id))
    get_db.execute(delete(User).where(usr_id == User.id))
    get_db.commit()
    return {
        "status_code":status.HTTP_200_OK,
        "transaction": f"User {usr_id} removed"
    }