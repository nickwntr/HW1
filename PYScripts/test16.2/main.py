import fastapi as fst
from fastapi import FastAPI
from typing import Annotated
app = FastAPI()


@app.get("/usr/adm")
async def getadmin():
    return "Вы вошли как администратор"

@app.get("/usr/{usrname}/{age}")
async def usrinfo(usrname: Annotated[str,fst.Path(min_length=5,max_length=20,description="Enter Username",example="DefUser")],
                  age: Annotated[int,fst.Path(ge=18,le=120,description="Enter age",example="24")]):
    return f"Информация о пльзователе: Пользователь: {usrname}, Возраст: {age}"

@app.get("/usr/{usrid}")
async def getuser(usrid: Annotated[int,fst.Path(ge=1,le=100,description="Enter your ID",example=1)]):
    return f"Вы вошли как {usrid}"


@app.get("/")
async def welcome():
    return "Главная страница"

#python -m uvicorn main:app

