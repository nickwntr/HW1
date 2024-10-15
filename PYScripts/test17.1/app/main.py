from fastapi import FastAPI
from routers import task
from routers import user
import uvicorn

app = FastAPI()
app.include_router(task.taskrouter)
app.include_router(user.userrouter)


@app.get("/")
async def welcome():
    return {"message": "Welcome to taskmanager"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)