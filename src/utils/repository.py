from abc import ABC, abstractmethod

from sqlalchemy import Insert, Select
from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.query import AbstractFilter


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

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_all(self, values: list[dict]):
        stmt = Insert(self.model).values(**values).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def add_one(self, values: dict):
        stmt = Insert(self.model).values(**values).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def get_all(self, filters: AbstractFilter, limits: AbstractFilter):
        query = Select(self.model)
        filters.apply(query)
        limits.apply(query)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_one(self, filters: AbstractFilter, limits: AbstractFilter):
        query = Select(self.model)
        filters.apply(query)
        limits.apply(query)
        result = await self.session.execute(query)
        return result.scalar_one()
