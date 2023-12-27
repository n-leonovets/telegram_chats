from pydantic_settings import SettingsConfigDict

from src.schemas import ChatResponse, CategoryResponse


class ChatFullResponse(ChatResponse):
    categories: list[CategoryResponse] = []
    model_config = SettingsConfigDict(
        from_attributes=True
    )
