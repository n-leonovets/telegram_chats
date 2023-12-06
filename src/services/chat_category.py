from typing import Optional

from src.models.chat import ChatModel
from src.schemas.chat import ChatResponse, ChatAdd, ChatUpdate
from src.services.filters.base import LimitFilter
from src.services.filters.chat import ChatFilter
from src.utils.unitofwork import AbstractUnitOfWork


class ChatCategoryService:
    @staticmethod
    async def add_chat_category(uow: AbstractUnitOfWork, chat: ChatAdd) -> ChatResponse:
        async with uow:
            result: ChatModel = await uow.chat_category.create_one(values=chat.model_dump())
            await uow.commit()
            return ChatResponse(**result.__dict__)

    @staticmethod
    async def add_chat_categories(uow: AbstractUnitOfWork, chats: list[ChatAdd]) -> list[ChatResponse]:
        async with uow:
            result: list[ChatModel] = await uow.chat_category.create_all(values=[chat.model_dump() for chat in chats])
            await uow.commit()
            return [ChatResponse(**chat.__dict__) for chat in result]

    @staticmethod
    async def get_chats_categories(
        uow: AbstractUnitOfWork,
        filters: Optional[ChatFilter] = None,
        limits: Optional[LimitFilter] = None
    ) -> list[ChatResponse]:
        async with uow:
            result: list[ChatModel] = await uow.chat_category.read_all(filters=filters, limits=limits)
            return [ChatResponse(**chat.__dict__) for chat in result]

    @staticmethod
    async def update_chat_category(uow: AbstractUnitOfWork, chat: ChatUpdate, filters: ChatFilter) -> ChatResponse:
        async with uow:
            result: ChatModel = await uow.chat_category.update_one(
                values=chat.model_dump(exclude_none=True),
                filters=filters
            )
            await uow.commit()
            return ChatResponse(**result.__dict__)

    @staticmethod
    async def delete_chat_category(uow: AbstractUnitOfWork, filters: ChatFilter) -> ChatResponse:
        async with uow:
            result: ChatModel = await uow.chat_category.delete_one(filters=filters)
            await uow.commit()
            return ChatResponse(**result.__dict__)
