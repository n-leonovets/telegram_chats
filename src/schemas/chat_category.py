from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict


class ChatCategorySchema(BaseModel):
    chat_id: int
    category: str

    model_config = SettingsConfigDict(
        from_attributes=True
    )
