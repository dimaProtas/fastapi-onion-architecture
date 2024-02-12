from abc import ABC, abstractmethod

from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from db.db import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

    @abstractmethod
    async def update_one(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session


    async def add_one(self, data: dict) -> dict:
        stmt = insert(self.model).values(**data).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def find_all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        # print(res.mappings().all())
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def find_one(self, id: int):
        query = select(self.model).filter_by(id=id)
        res = await self.session.execute(query)
        res = res.scalar_one().to_read_model()
        return res

    async def update_one(self, id: int, data: dict) -> dict:
        stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one()
