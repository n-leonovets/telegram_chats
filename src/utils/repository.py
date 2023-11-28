from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy import Insert, Select, Update, Delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.query import AbstractFilter


class AbstractRepository(ABC):
    @abstractmethod
    async def create_all(self, values: list[dict]):
        raise NotImplementedError

    @abstractmethod
    async def create_one(self, values: dict):
        raise NotImplementedError

    @abstractmethod
    async def read_all(self, filters: Optional[AbstractFilter] = None, limits: Optional[AbstractFilter] = None):
        raise NotImplementedError

    @abstractmethod
    async def read_one(self, filters: Optional[AbstractFilter] = None, limits: Optional[AbstractFilter] = None):
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, values: dict, filters: AbstractFilter):
        raise NotImplementedError

    async def delete_one(self, filters: AbstractFilter):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_one(self, values: dict):
        stmt = Insert(self.model).values(**values).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def create_all(self, values: list[dict]):
        stmt = Insert(self.model).values(values).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def read_one(self, filters: Optional[AbstractFilter] = None, limits: Optional[AbstractFilter] = None):
        query = Select(self.model)
        if filters:
            query = filters.apply(query)
        if limits:
            query = limits.apply(query)
        result = await self.session.execute(query)
        return result.scalar_one()

    async def read_all(self, filters: Optional[AbstractFilter] = None, limits: Optional[AbstractFilter] = None):
        query = Select(self.model)
        if filters:
            query = filters.apply(query)
        if limits:
            query = limits.apply(query)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def update_one(self, values: dict, filter_by: dict):
        stmt = Update(self.model).values(**values).filter_by(**filter_by).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def delete_one(self, filter_by: dict):
        stmt = Delete(self.model).filter_by(**filter_by).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar_one()
