from schemas.tasks import TaskSchemaAdd, TaskHistorySchemaAdd, TaskSchema
from utils.unitofwork import IUnitOfWork


class TasksService:

    async def add_task(self, uow: IUnitOfWork, task: TaskSchemaAdd):
        async with uow:
            tasks_dict = task.model_dump()
            task = await uow.tasks.add_one(tasks_dict)
            await uow.commit()
            return task

    async def get_tasks(self, uow: IUnitOfWork):
        async with uow:
            tasks = await uow.tasks.find_all()
            return tasks

    async def get_histroy(self, uow: IUnitOfWork):
        async with uow:
            history = await uow.task_history.find_all()
            return history

    async def edit_task(self, task_id: int, task: TaskSchemaAdd,  uow: IUnitOfWork):
        task_dict = task.model_dump()
        async with uow:
            res = await uow.tasks.update_one(task_id, task_dict)
            curr_task = await uow.tasks.find_one(id=task_id)
            task_history_log = TaskHistorySchemaAdd(
                task_id=task_id,
                previous_assignee_id=curr_task.assignee_id,
                new_assignee_id=task.assignee_id,
            )
            task_history_log = task_history_log.model_dump()
            print(task_history_log)
            await uow.task_history.add_one(task_history_log)
            await uow.commit()
            return res
