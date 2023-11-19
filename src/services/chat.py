from src.models.chat import ChatTable
from src.schemas.chat import ChatModel
from src.utils.query import ChatFilter, LimitFilter
from src.utils.repository import AbstractRepository


class ChatService:
    def __init__(self, chat_repo: AbstractRepository):
        self.chat_repo: AbstractRepository = chat_repo

    async def add_chat(self, chat: ChatModel) -> ChatModel:
        chat: ChatTable = await self.chat_repo.add_one(values=chat.model_dump())
        return ChatModel(**chat.__dict__)

    async def get_chats(self, filters: ChatFilter, limits: LimitFilter) -> list[ChatModel]:
        chats: list[ChatTable] = await self.chat_repo.get_all(filters=filters, limits=limits)
        return [ChatModel(**chat.__dict__) for chat in chats]
