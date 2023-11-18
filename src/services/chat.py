from src_base.models.chat import ChatTable
from src_base.schemas.chat import ChatModel
from src_base.utils.query import ChatFilter, LimitFilter
from src_base.utils.repository import AbstractRepository


class ChatService:
    def __init__(self, chat_repo: AbstractRepository):
        self.chat_repo: AbstractRepository = chat_repo

    async def add_chat(self, chat: ChatModel) -> ChatModel:
        chat: ChatTable = await self.chat_repo.add_one(values=chat.model_dump())
        return ChatModel(**chat.__dict__)

    async def get_chats(self, filters: ChatFilter, limits: LimitFilter) -> list[ChatModel]:
        chats: list[ChatTable] = await self.chat_repo.get_all(filters=filters, limits=limits)
        return [ChatModel(**chat.__dict__) for chat in chats]
