from fastapi import FastAPI, APIRouter, HTTPException

from src.dependencies import TaskServiceDep
from src.schema import TaskSchema




tasks_router = APIRouter(prefix='/tasks')


@tasks_router.post('/create-task')
async def create_task(task:TaskSchema, service: TaskServiceDep):
    await service.create_task(task)
    return {"result" : "OK"}

@tasks_router.get('/get-task-list')
async def get_task_list(service: TaskServiceDep):
    result = await service.get_all_tasks()
    return { "result" : result}

@tasks_router.delete('/delete-task')
async def delete_task(task: TaskSchema, service: TaskServiceDep):
    await service.delete_task(task)
    return {"result" : "OK"}

@tasks_router.post('/check-task')
async def check_task(task: TaskSchema, service: TaskServiceDep):
    result = await service.get_task(task)
    return {"result" : result}
