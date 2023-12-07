import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict


class Category(BaseModel):
    name: str
    parent_id: Optional[int] = 0


class CategoryResponse(BaseModel):
    id: int
    name: str
    parent_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    model_config = SettingsConfigDict(
        from_attributes=True
    )


class CategoryFullResponse(CategoryResponse):
    chats: 'list[ChatResponse]' = []
    model_config = SettingsConfigDict(
        from_attributes=True
    )


from src.schemas.chat import ChatResponse
CategoryFullResponse.model_rebuild()
