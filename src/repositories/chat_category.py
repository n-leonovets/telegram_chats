from src.models import ChatCategoryModel
from src.utils.repository import SQLAlchemyRepository


class ChatCategoryRepository(SQLAlchemyRepository):
    model = ChatCategoryModel
