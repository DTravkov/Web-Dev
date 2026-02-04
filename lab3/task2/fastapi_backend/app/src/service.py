from fastapi import HTTPException
from src.dependencies import TaskRepository
from src.schema import TaskSchema
from src.model import TaskModel

from core.logging import get_logger
logger = get_logger(__name__)



class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    async def create_task(self, task: TaskSchema) -> TaskSchema:
        model: TaskModel = await self.repo.get_task(task.task_name)

        if model:
            raise HTTPException(status_code=403, detail="Already exists")
        
        await self.repo.create_task(task.task_name)

        return task

    async def get_all_tasks(self):
        result = await self.repo.get_all_tasks()
        return result

    async def delete_task(self, task: TaskSchema):
        model: TaskModel = await self.repo.get_task(task.task_name)
        if(not model):
            raise HTTPException(status_code=404, detail="Task not found")
        
        try:
            await self.repo.delete_task(model)
        except Exception:
            await self.repo.session.rollback()
            raise HTTPException(status_code=500, detail="Something went wrong while deleting the task")
    
    async def get_task(self, task: TaskSchema):
        result = await self.repo.get_task(task.task_name)
        return bool(result)

