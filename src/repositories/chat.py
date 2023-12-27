from src.models import ChatModel
from src.utils.repository import SQLAlchemyRepository


class ChatRepository(SQLAlchemyRepository):
    model = ChatModel
