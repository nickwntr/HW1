import fastapi as fst
from fastapi import FastAPI
from typing import Annotated
users = {'1':"Имя: Example, возраст:18"}
app = FastAPI()

@app.get("/usr/adm")
async def getadmin():
    return "Вы вошли как администратор"

@app.put("/usr/{usrid}/{usrname}/{age}")
async def update(usrid: str,
                 usrname: Annotated[str, fst.Path(min_length=3,max_length=50,description="Enter Username",example="DefUser")],
                 age: Annotated[int, fst.Path(ge=18,le=120,description="Enter age",example="24")]):
    users[usrid] = f"Имя: {usrname}, возраст:{age}"
    return f"The user {usrid} is registred"


@app.post("/addusr/{usrname}/{age}")
async def addusr(usrname: Annotated[str, fst.Path(min_length=3,max_length=50,description="Enter Username",example="DefUser")],
                  age: Annotated[int, fst.Path(ge=18,le=120,description="Enter age",example="24")]):
    i = str(int(max(users,key=int))+1)
    users[i] = f"Имя: {usrname}, возраст:{age}"
    return f"User {i} is registred"

@app.get("/usr/{usrname}/{age}")
async def usrinfo(usrname: Annotated[str,fst.Path(min_length=5,max_length=20,description="Enter Username",example="DefUser")],
                  age: Annotated[int,fst.Path(ge=18,le=120,description="Enter age",example="24")]):
    return f"Информация о пльзователе: Пользователь: {usrname}, Возраст: {age}"

@app.delete("/usr/{usrid}")
async def dropuser(usrid: str):

    users.pop(usrid)
    return 0

@app.get("/usr/{usrid}")
async def getuser(usrid: Annotated[int,fst.Path(ge=1,le=100,description="Enter your ID",example=1)]):
    return f"Вы вошли как {usrid}"

@app.get("/users")
async def getuser():
    return users

@app.get("/")
async def welcome():
    return "Главная страница"

#python -m uvicorn main:app

