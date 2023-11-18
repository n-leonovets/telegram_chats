from src_base.models.chat import ChatTable
from src_base.utils.repository import SQLAlchemyRepository


class ChatRepository(SQLAlchemyRepository):
    model = ChatTable
