
from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.repository import TaskRepository
from src.service import TaskService


def get_task_repo(session: AsyncSession = Depends(get_db)):
    return TaskRepository(session)

TaskRepositoryDep = Annotated[TaskRepository, Depends(get_task_repo)]

def get_task_service(repo: TaskRepositoryDep):
    return TaskService(repo)

TaskServiceDep = Annotated[TaskService, Depends(get_task_service)]


