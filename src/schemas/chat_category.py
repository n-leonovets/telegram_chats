import datetime

from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict


class ChatCategoryResponse(BaseModel):
    chat_id: int
    category_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    model_config = SettingsConfigDict(
        from_attributes=True
    )


class ChatCategory(BaseModel):
    chat_id: int
    category_id: int

    model_config = SettingsConfigDict(
        from_attributes=True
    )
