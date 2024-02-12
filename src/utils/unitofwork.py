from abc import ABC, abstractmethod
from typing import Type
from db.db import async_session_maker
from repositories.users import UsersRepository
from repositories.tasks import TasksRepository
from repositories.task_history import TasksHistoryRepository
from repositories.cars import CarsRepository


class IUnitOfWork(ABC):
    users: Type[UsersRepository]
    tasks: Type[TasksRepository]
    task_history: Type[TasksHistoryRepository]
    cars: Type[CarsRepository]

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.users = UsersRepository(self.session)
        self.tasks = TasksRepository(self.session)
        self.task_history = TasksHistoryRepository(self.session)
        self.cars = CarsRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
