import datetime
from typing import Optional, Annotated

from pydantic import BaseModel, StringConstraints
from pydantic_settings import SettingsConfigDict


class ChatModel(BaseModel):
    id: int
    username: Optional[str] = None
    invite_link: Optional[str] = None
    members_count: Optional[int] = 0
    title: Annotated[str, StringConstraints(max_length=255)]
    description: Optional[Annotated[str, StringConstraints(max_length=255)]] = None
    is_verified: bool
    is_restricted: bool
    is_scam: bool
    is_fake: bool
    is_forum: bool
    is_moderated: bool
    is_closed: bool
    updated_at: Optional[datetime.datetime] = datetime.datetime.now()

    model_config = SettingsConfigDict(
        from_attributes=True
    )


class AddChatModel(BaseModel):
    id: int
    username: Optional[str] = None
    invite_link: Optional[str] = None
    members_count: Optional[int] = 0
    title: Annotated[str, StringConstraints(max_length=255)] = None
    description: Optional[Annotated[str, StringConstraints(max_length=255)]] = None
    is_verified: Optional[bool] = False
    is_restricted: Optional[bool] = False
    is_scam: Optional[bool] = False
    is_fake: Optional[bool] = False
    is_forum: Optional[bool] = False
    is_moderated: Optional[bool] = False
    is_closed: Optional[bool] = False

    model_config = SettingsConfigDict(
        from_attributes=True
    )


class UpdateChat(ChatModel):

    model_config = SettingsConfigDict()
