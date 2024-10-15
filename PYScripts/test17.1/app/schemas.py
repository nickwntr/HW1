from pydantic import BaseModel
from pydantic import schema


class CreateUser(BaseModel):
    username: str = None
    frstname: str = None
    lastname: str = None
    age: str = None


class UpdateUser(BaseModel):
    frstname: str = None
    lastname: str = None
    age: str = None


class CreateTask(BaseModel):
    title: str = None
    content: str = None
    priority: str = None
