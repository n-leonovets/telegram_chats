from pydantic_settings import SettingsConfigDict

from src.schemas.category import CategoryResponse
from src.schemas.chat import ChatResponse


class CategoryFullResponse(CategoryResponse):
    chats: list[ChatResponse] = []

    model_config = SettingsConfigDict(
        from_attributes=True
    )
