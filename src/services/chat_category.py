from typing import Optional

from src.schemas import ChatCategory, ChatCategoryResponse
from src.services.filters import LimitFilter, ChatCategoryFilter
from src.utils.unitofwork import AbstractUnitOfWork


class ChatCategoryService:
    @staticmethod
    async def add_chat_category(
        uow: AbstractUnitOfWork,
        chat_category: ChatCategory
    ) -> ChatCategoryResponse:
        async with uow:
            result: ChatCategory = await uow.chat_category.create_one(values=chat_category.model_dump())
            await uow.commit()
            return ChatCategoryResponse.model_validate(result, from_attributes=True)

    @staticmethod
    async def add_chat_categories(
        uow: AbstractUnitOfWork,
        chat_categories: list[ChatCategory]
    ) -> list[ChatCategoryResponse]:
        async with uow:
            result: list[ChatCategory] = await uow.chat_category.create_all(
                values=[chat_category.model_dump() for chat_category in chat_categories]
            )
            await uow.commit()
            return [ChatCategoryResponse.model_validate(chat, from_attributes=True) for chat in result]

    @staticmethod
    async def get_chat_categories(
        uow: AbstractUnitOfWork,
        filters: Optional[ChatCategoryFilter] = None,
        limits: Optional[LimitFilter] = None
    ) -> list[ChatCategoryResponse]:
        async with uow:
            result: list[ChatCategory] = await uow.chat_category.read_all(filters=filters, limits=limits)
            return [ChatCategoryResponse.model_validate(chat, from_attributes=True) for chat in result]

    @staticmethod
    async def update_chat_category(
        uow: AbstractUnitOfWork,
        chat_category: ChatCategory,
        filters: ChatCategoryFilter
    ) -> ChatCategoryResponse:
        async with uow:
            result: ChatCategory = await uow.chat_category.update_one(
                values=chat_category.model_dump(exclude_none=True),
                filters=filters
            )
            await uow.commit()
            return ChatCategoryResponse.model_validate(result, from_attributes=True)

    @staticmethod
    async def delete_chat_category(
        uow: AbstractUnitOfWork,
        filters: ChatCategoryFilter
    ) -> ChatCategoryResponse:
        async with uow:
            result: ChatCategory = await uow.chat_category.delete_one(filters=filters)
            await uow.commit()
            return ChatCategoryResponse.model_validate(result, from_attributes=True)
