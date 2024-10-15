from fastapi import FastAPI

app = FastAPI()


@app.get("/usr/adm")
async def getadmin():
    return "Вы вошли как администратор"

@app.get("/usr/{usrid}")
async def getusr(usrid):
    return f"Вы вошли как {usrid}"

@app.get("/usr")
async def usrinfo(usrname,age):
    return f"Информация о пльзователе: Пользователь: {usrname}, Возраст: {age}"

@app.get("/")
async def welcome():
    return "Главная страница"

#python -m uvicorn main:app

