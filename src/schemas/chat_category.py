from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict


class ChatCategoryModel(BaseModel):
    chat_id: int
    category: str

    model_config = SettingsConfigDict(
        from_attributes=True
    )
