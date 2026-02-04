
from fastapi import HTTPException

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.model import TaskModel
from core.logging import get_logger
logger = get_logger(__name__)

class TaskRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_task(self, task_name: str) -> TaskModel:
        task = await self.session.get(TaskModel, task_name)
        return task
    
    async def create_task(self, task_name:str) -> TaskModel:
        task = TaskModel(task_name=task_name)
        self.session.add(task)
        await self.session.flush()
        return task
    
    
    async def update_task(self, task: TaskModel, **kwargs) -> TaskModel:
       
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)
        
        return task

    async def get_all_tasks(self):
        result = await self.session.scalars(select(TaskModel))
        result = list(map(lambda x: x.task_name, result.all()))
        return result
    
    async def delete_task(self, task: TaskModel):
        await self.session.delete(task)
        await self.session.flush()
    


