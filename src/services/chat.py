from src.models.chat import ChatTable
from src.schemas.chat import ChatModel
from src.utils.query import ChatFilter, LimitFilter
from src.utils.unitofwork import AbstractUnitOfWork


class ChatService:
    @staticmethod
    async def add_chat(uow: AbstractUnitOfWork, chat: ChatModel) -> ChatModel:
        async with uow:
            chat: ChatTable = await uow.chat.add_one(values=chat.model_dump())
            await uow.commit()
            return ChatModel(**chat.__dict__)

    @staticmethod
    async def get_chats(uow: AbstractUnitOfWork, filters: ChatFilter, limits: LimitFilter) -> list[ChatModel]:
        async with uow:
            chats: list[ChatTable] = await uow.chat.get_all(filters=filters, limits=limits)
            return [ChatModel(**chat.__dict__) for chat in chats]
