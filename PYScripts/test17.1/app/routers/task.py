from fastapi import APIRouter

taskrouter = APIRouter(prefix="/user", tags=["user"])


@taskrouter.get("/")
async def all_tasks():
    pass

@taskrouter.get("/task_id")
async def task_by_id():
    pass

@taskrouter.post("/create")
async def create_task():
    pass

@taskrouter.put("/update")
async def update_task():
    pass

@taskrouter.delete("/delete")
async def delete_task():
    pass