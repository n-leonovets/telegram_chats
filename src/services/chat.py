from src.models.chat import ChatTable
from src.schemas.chat import ChatModel, ChatAddModel, ChatUpdateModel
from src.utils.query import ChatFilter, LimitFilter
from src.utils.unitofwork import AbstractUnitOfWork


class ChatService:
    @staticmethod
    async def add_chat(uow: AbstractUnitOfWork, chat: ChatAddModel) -> ChatModel:
        async with uow:
            result: ChatTable = await uow.chat.create_one(values=chat.model_dump())
            await uow.commit()
            return ChatModel(**result.__dict__)

    @staticmethod
    async def add_chats(uow: AbstractUnitOfWork, chats: list[ChatAddModel]) -> list[ChatModel]:
        async with uow:
            result: list[ChatTable] = await uow.chat.create_all(values=[chat.model_dump() for chat in chats])
            await uow.commit()
            return [ChatModel(**chat.__dict__) for chat in result]

    @staticmethod
    async def get_chats(uow: AbstractUnitOfWork, filters: ChatFilter, limits: LimitFilter) -> list[ChatModel]:
        async with uow:
            result: list[ChatTable] = await uow.chat.read_all(filters=filters, limits=limits)
            return [ChatModel(**chat.__dict__) for chat in result]

    @staticmethod
    async def update_chat(uow: AbstractUnitOfWork, chat: ChatUpdateModel, filter_by: dict) -> ChatModel:
        async with uow:
            result: ChatTable = await uow.chat.update_one(
                values=chat.model_dump(exclude_none=True),
                filter_by=filter_by
            )
            await uow.commit()
            return ChatModel(**result.__dict__)

    @staticmethod
    async def delete_chat(uow: AbstractUnitOfWork, filter_by: dict) -> ChatModel:
        async with uow:
            result: ChatTable = await uow.chat.delete_one(filter_by=filter_by)
            await uow.commit()
            return ChatModel(**result.__dict__)
