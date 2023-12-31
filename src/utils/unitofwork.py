from abc import ABC, abstractmethod

from src.database import async_session_maker
from src.repositories.chat import ChatRepository
from src.repositories.category import CategoryRepository
from src.repositories.chat_category import ChatCategoryRepository
from src.repositories.user import UserRepository


class AbstractUnitOfWork(ABC):
    chat: ChatRepository
    category: CategoryRepository
    chat_category: ChatCategoryRepository
    user: UserRepository

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


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.chat = ChatRepository(self.session)
        self.category = CategoryRepository(self.session)
        self.chat_category = ChatCategoryRepository(self.session)
        self.user = UserRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
