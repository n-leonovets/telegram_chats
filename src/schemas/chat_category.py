import datetime

from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict

from src.schemas.base import DatetimeBaseModel


class ChatCategoryResponse(DatetimeBaseModel):
    chat_id: int
    category: str

    model_config = SettingsConfigDict(
        from_attributes=True
    )


class ChatCategory(BaseModel):
    chat_id: int
    category: str

    model_config = SettingsConfigDict(
        from_attributes=True
    )
