from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_async_session
from models.tasks import Task
from services.tasks import TasksService
from api.dependencies import tasks_service
from schemas.tasks import TaskSchemaAdd


router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)


# @router.get('/get_tasks')
# async def get_tasks(session: AsyncSession = Depends(get_async_session)):
#     queryset = select(Task)
#     result = await session.execute(queryset)
#     return {"tags": result.mappings().all()}
#
#
# @router.post('/add_task')
# async def add_post(new_task: TaskSchemaAdd, session: AsyncSession = Depends(get_async_session)):
#     try:
#         statement = insert(Task).values(**new_task.dict())
#         await session.execute(statement)
#         await session.commit()
#         return {'status': 'ok', 'task': new_task}
#     except Exception:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={
#             'status': 'error'
#         })


@router.get('/get_tasks')
async def get_tasks(
    tasks_service: Annotated[TasksService, Depends(tasks_service)],
):
    tasks = await tasks_service.get_tasks()
    return tasks

@router.post('add_task')
async def add_task(task: TaskSchemaAdd, task_service: Annotated[TasksService, Depends(tasks_service)]):
    task = await task_service.add_task(task)
    return task