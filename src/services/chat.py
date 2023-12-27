from typing import Optional

from src.models.chat import ChatModel
from src.schemas.chat import ChatResponse, ChatFullResponse, ChatAdd, ChatUpdate
from src.services.filters.base import LimitFilter
from src.services.filters.chat import ChatFilter
from src.utils.unitofwork import AbstractUnitOfWork


class ChatService:
    @staticmethod
    async def add_chat(uow: AbstractUnitOfWork, chat: ChatAdd) -> ChatResponse:
        async with uow:
            result: ChatModel = await uow.chat.create_one(values=chat.model_dump())
            await uow.commit()
            return ChatResponse.model_validate(result, from_attributes=True)

    @staticmethod
    async def add_chats(uow: AbstractUnitOfWork, chats: list[ChatAdd]) -> list[ChatResponse]:
        async with uow:
            result: list[ChatModel] = await uow.chat.create_all(values=[chat.model_dump() for chat in chats])
            await uow.commit()
            return [ChatResponse.model_validate(row, from_attributes=True) for row in result]

    @staticmethod
    async def get_chats(
        uow: AbstractUnitOfWork,
        filters: Optional[ChatFilter] = None,
        limits: Optional[LimitFilter] = None
    ) -> list[ChatFullResponse]:
        async with uow:
            result: list[ChatModel] = await uow.chat.read_all(filters=filters, limits=limits)
            return [ChatFullResponse.model_validate(row, from_attributes=True) for row in result]

    @staticmethod
    async def update_chat(uow: AbstractUnitOfWork, chat: ChatUpdate, filters: ChatFilter, exclude_none: bool = True) -> ChatResponse:
        async with uow:
            result: ChatModel = await uow.chat.update_one(
                values=chat.model_dump(exclude_none=exclude_none),
                filters=filters
            )
            await uow.commit()
            return ChatResponse.model_validate(result, from_attributes=True)

    @staticmethod
    async def update_chats(uow: AbstractUnitOfWork, chat: ChatUpdate, filters: ChatFilter) -> list[ChatResponse]:
        async with uow:
            result: list[ChatModel] = await uow.chat.update_many(
                values=chat.model_dump(exclude_none=True),
                filters=filters
            )
            await uow.commit()
            return [ChatFullResponse.model_validate(row, from_attributes=True) for row in result]

    @staticmethod 
    async def delete_chats(uow: AbstractUnitOfWork, filters: ChatFilter):
        async with uow:
            await uow.chat.delete_many(filters=filters)
            await uow.commit()

    @staticmethod
    async def delete_chat(uow: AbstractUnitOfWork, filters: ChatFilter) -> ChatResponse:
        async with uow:
            result: ChatModel = await uow.chat.delete_one(filters=filters)
            await uow.commit()
            return ChatResponse.model_validate(result, from_attributes=True)
