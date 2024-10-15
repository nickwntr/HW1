from pydantic import BaseModel
from pydantic import schema


class CreateUser(BaseModel):
    username: str = None
    frstname: str = None
    lastname: str = None
    age: int = None


class UpdateUser(BaseModel):
    frstname: str = None
    lastname: str = None
    age: int = None


class CreateTask(BaseModel):
    title: str = None
    content: str = None
    priority: int = None

class UpdateTask(BaseModel):
    title: str = None
    content: str = None
    priority: int = None
