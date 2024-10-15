import fastapi as fst
import uvicorn
from fastapi import FastAPI, Request
from typing import Annotated
from pydantic import BaseModel
from pydantic import Field
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="temps")


class User(BaseModel):
    id: int = Field()
    username: str = Field()
    age: int = Field()


users = [
    User(id=1, username="N1cky", age=22),
    User(id=2, username="Jack", age=20),
    User(id=3, username="Boise", age=77),

]

app = FastAPI()


@app.get("/usr/adm")
async def getadmin():
    return "Вы вошли как администратор"


@app.put("/usr/{usrid}/{usrname}/{age}")
async def update(usrid: int,
                 usrname: Annotated[str, fst.Path(min_length=3,max_length=50,description="Enter Username",example="DefUser")],
                 age: Annotated[int, fst.Path(ge=18,le=120,description="Enter age",example="24")]):
    try:
        found = False
        for user in users:
            if user.id == usrid:
                found = True
                print(user)
                ind = users.index(user)
                users.remove(user)
                users.insert(ind,User(id = usrid, username = usrname, age = age))
                break
        if not found:
            raise IndexError
    except IndexError:
        raise fst.HTTPException(status_code=404,detail=f"User {usrid} not found")
    return f"The user {usrid} is registred"


@app.post("/addusr/{usrname}/{age}")
async def addusr(usrname: Annotated[str, fst.Path(min_length=3,max_length=50,description="Enter Username",example="DefUser")],
                 age: Annotated[int, fst.Path(ge=18,le=120,description="Enter age",example="24")]):
    i = len(users) + 1
    users.append(User(id = i, username = usrname, age = age))
    return f"User {i} is registred"


@app.get("/usr/{usrname}/{age}")
async def usrinfo(usrname: Annotated[str,fst.Path(min_length=5,max_length=20,description="Enter Username",example="DefUser")],
                  age: Annotated[int,fst.Path(ge=18,le=120,description="Enter age",example="24")]):
    return f"Информация о пльзователе: Пользователь: {usrname}, Возраст: {age}"


@app.delete("/usr/{usrid}")
async def dropuser(usrid: int):
    try:
        found = False
        for user in users:
            if user.id == usrid:
                found = True
                dUser = user
                users.remove(dUser)
                return dUser

        if not found:
            raise IndexError
    except IndexError:
        raise fst.HTTPException(status_code=404, detail=f"User {usrid} not found")


@app.get("/users/{usrid}")
async def getuser(request : Request,usrid: Annotated[int,fst.Path(ge=1,le=100,description="Enter your ID",example=1)]):
    try:
        found = False
        for user in users:
            if user.id == usrid:
                found = True
                return templates.TemplateResponse("users.html",{"request":request,"user":user})
        if not found:
            raise IndexError
    except IndexError:
        raise fst.HTTPException(status_code=404, detail=f"User {usrid} not found")
    return templates.TemplateResponse("users.html",{"request":request,"user":user})

@app.get("/users")
async def getuser():
    return users

@app.get("/")
async def welcome(request: Request):
    return templates.TemplateResponse("users.html",{"request":request,"users":users})


# python -m uvicorn main:app
if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
