from src.models.chat_category import ChatCategoryModel
from src.utils.repository import SQLAlchemyRepository


class ChatCategoryRepository(SQLAlchemyRepository):
    model = ChatCategoryModel
