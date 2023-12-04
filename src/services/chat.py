from typing import Optional

from src.models.chat import ChatModel
from src.schemas.chat import ChatSchema, ChatAddSchema, ChatUpdateSchema
from src.services.filters.base import LimitFilter
from src.services.filters.chat import ChatFilter
from src.utils.unitofwork import AbstractUnitOfWork


class ChatService:
    @staticmethod
    async def add_chat(uow: AbstractUnitOfWork, chat: ChatAddSchema) -> ChatSchema:
        async with uow:
            result: ChatModel = await uow.chat.create_one(values=chat.model_dump())
            await uow.commit()
            return ChatSchema(**result.__dict__)

    @staticmethod
    async def add_chats(uow: AbstractUnitOfWork, chats: list[ChatAddSchema]) -> list[ChatSchema]:
        async with uow:
            result: list[ChatModel] = await uow.chat.create_all(values=[chat.model_dump() for chat in chats])
            await uow.commit()
            return [ChatSchema(**chat.__dict__) for chat in result]

    @staticmethod
    async def get_chats(
        uow: AbstractUnitOfWork,
        filters: Optional[ChatFilter] = None,
        limits: Optional[LimitFilter] = None
    ) -> list[ChatSchema]:
        async with uow:
            result: list[ChatModel] = await uow.chat.read_all(filters=filters, limits=limits)
            return [ChatSchema(**chat.__dict__) for chat in result]

    @staticmethod
    async def update_chat(uow: AbstractUnitOfWork, chat: ChatUpdateSchema, filters: ChatFilter) -> ChatSchema:
        async with uow:
            result: ChatModel = await uow.chat.update_one(
                values=chat.model_dump(exclude_none=True),
                filters=filters
            )
            await uow.commit()
            return ChatSchema(**result.__dict__)

    @staticmethod
    async def delete_chat(uow: AbstractUnitOfWork, filters: ChatFilter) -> ChatSchema:
        async with uow:
            result: ChatModel = await uow.chat.delete_one(filters=filters)
            await uow.commit()
            return ChatSchema(**result.__dict__)
