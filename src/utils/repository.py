from abc import ABC, abstractmethod

from sqlalchemy import Insert, Select

from src_base.database import async_session_maker
from src_base.utils.query import AbstractFilter


class AbstractRepository(ABC):
    @abstractmethod
    async def add_all(self, values: list[dict]):
        raise NotImplementedError

    @abstractmethod
    async def add_one(self, values: dict):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, filters: AbstractFilter, limits: AbstractFilter):
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, filters: AbstractFilter, limits: AbstractFilter):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_all(self, values: list[dict]):
        async with async_session_maker() as session:
            stmt = Insert(self.model).values(**values).returning(self.model)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalars().all()

    async def add_one(self, values: dict):
        async with async_session_maker() as session:
            stmt = Insert(self.model).values(**values).returning(self.model)
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar_one()

    async def get_all(self, filters: AbstractFilter, limits: AbstractFilter):
        async with async_session_maker() as session:
            query = Select(self.model)
            filters.apply(query)
            limits.apply(query)
            result = await session.execute(query)
            return result.scalars().all()

    async def get_one(self, filters: AbstractFilter, limits: AbstractFilter):
        async with async_session_maker() as session:
            query = Select(self.model)
            filters.apply(query)
            limits.apply(query)
            result = await session.execute(query)
            return result.scalar_one()
