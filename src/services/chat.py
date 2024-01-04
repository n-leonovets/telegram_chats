from typing import Optional

from src.models import ChatModel
from src.schemas import ChatResponse, ChatFullResponse, ChatAdd, ChatUpdate
from src.services.filters import LimitFilter, ChatFilter, ChatListFilter
from src.utils.unitofwork import AbstractUnitOfWork


class ChatService:
    @staticmethod
    async def add_chat(
        uow: AbstractUnitOfWork,
        chat: ChatAdd
    ) -> ChatResponse:
        async with uow:
            result: ChatModel = await uow.chat.create_one(values=chat.model_dump())
            await uow.commit()
            return ChatResponse.model_validate(result, from_attributes=True)

    @staticmethod
    async def get_chat(
        uow: AbstractUnitOfWork,
        filters: ChatFilter = None
    ) -> ChatFullResponse:
        async with uow:
            result: ChatModel = await uow.chat.read_one(filters=filters)
            return ChatFullResponse.model_validate(result, from_attributes=True)

    @staticmethod
    async def update_chat(
        uow: AbstractUnitOfWork,
        chat: ChatUpdate,
        filters: ChatFilter
    ) -> ChatResponse:
        async with uow:
            result: ChatModel = await uow.chat.update_one(
                values=chat.model_dump(exclude_unset=True),
                filters=filters
            )
            await uow.commit()
            return ChatResponse.model_validate(result, from_attributes=True)

    @staticmethod
    async def delete_chat(
        uow: AbstractUnitOfWork,
        filters: ChatFilter
    ) -> ChatResponse:
        async with uow:
            result: ChatModel = await uow.chat.delete_one(filters=filters)
            await uow.commit()
            return ChatResponse.model_validate(result, from_attributes=True)

    @staticmethod
    async def add_chats(
        uow: AbstractUnitOfWork,
        chats: list[ChatAdd]
    ) -> list[ChatResponse]:
        async with uow:
            result: list[ChatModel] = await uow.chat.create_many(values=[chat.model_dump() for chat in chats])
            await uow.commit()
            return [
                ChatResponse.model_validate(
                    row,
                    from_attributes=True
                ) for row in result
            ]

    @staticmethod
    async def get_chats(
        uow: AbstractUnitOfWork,
        filters: Optional[ChatFilter] = None,
        limits: Optional[LimitFilter] = None
    ) -> list[ChatFullResponse]:
        async with uow:
            result: list[ChatModel] = await uow.chat.read_many(filters=filters, limits=limits)
            return [
                ChatFullResponse.model_validate(
                    row,
                    from_attributes=True
                ) for row in result
            ]

    @staticmethod
    async def update_chats(
        uow: AbstractUnitOfWork,
        chats: list[ChatUpdate],
        filters: ChatListFilter
    ) -> list[ChatResponse]:
        async with uow:
            result: list[ChatModel] = await uow.chat.update_many(
                values=[
                    chat.model_dump(exclude_unset=True)
                    for chat in chats
                ],
                filters=filters
            )
            await uow.commit()
            return [
                ChatResponse.model_validate(
                    chat,
                    from_attributes=True
                )
                for chat in result
            ]

    @staticmethod
    async def delete_chats(
        uow: AbstractUnitOfWork,
        filters: ChatListFilter
    ) -> list[ChatResponse]:
        async with uow:
            result: list[ChatModel] = await uow.chat.delete_many(filters=filters)
            await uow.commit()
            return [
                ChatResponse.model_validate(
                    chat,
                    from_attributes=True
                ) for chat in result
            ]
