from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_async_session
from models.tasks import Task
from services.tasks import TasksService
from api.dependencies import UOWDep
from schemas.tasks import TaskSchemaAdd, TaskSchema

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
async def get_tasks(uow: UOWDep):
    tasks = await TasksService().get_tasks(uow)
    return {"tasks": tasks}


@router.get('/history')
async def history(uow: UOWDep):
    history = await TasksService().get_histroy(uow)
    return {"history": history}


@router.post('/add_task')
async def add_task(task: TaskSchemaAdd, uow: UOWDep):
    task = await TasksService().add_task(uow, task)
    return {"task": task}


@router.patch('/edit_task/{task_id}')
async def edit_task(task_id: int, task: TaskSchemaAdd, uow: UOWDep):
    task_history = await TasksService().edit_task(task_id, task, uow)
    return {"task_history": task_history}

