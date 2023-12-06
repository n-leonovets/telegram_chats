import datetime

from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict

from src.schemas.category import CategoryResponse
from src.schemas.chat import ChatResponse


class ChatCategoryResponse(BaseModel):
    chat_id: ChatResponse
    category_id: CategoryResponse
    created_at: datetime.datetime
    updated_at: datetime.datetime

    model_config = SettingsConfigDict(
        from_attributes=True
    )


class ChatCategory(BaseModel):
    chat_id: int
    category_id: str

    model_config = SettingsConfigDict(
        from_attributes=True
    )
