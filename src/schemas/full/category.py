from pydantic_settings import SettingsConfigDict

from src.schemas import ChatResponse, CategoryResponse


class CategoryFullResponse(CategoryResponse):
    chats: list[ChatResponse] = []

    model_config = SettingsConfigDict(
        from_attributes=True
    )
