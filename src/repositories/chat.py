from src.models.chat import ChatTable
from src.utils.repository import SQLAlchemyRepository


class ChatRepository(SQLAlchemyRepository):
    model = ChatTable
