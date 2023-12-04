import datetime
from typing import Optional, Annotated

from pydantic import BaseModel, StringConstraints
from pydantic_settings import SettingsConfigDict


class ChatResponse(BaseModel):
    id: int
    username: Optional[str] = None
    invite_link: Optional[str] = None
    members_count: int
    title: Annotated[str, StringConstraints(max_length=255)]
    description: Optional[Annotated[str, StringConstraints(max_length=255)]] = None
    is_verified: bool
    is_restricted: bool
    is_scam: bool
    is_fake: bool
    is_forum: bool
    is_moderated: bool
    is_closed: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime

    model_config = SettingsConfigDict(
        from_attributes=True
    )


class ChatUpdate(BaseModel):
    username: Optional[str] = None
    invite_link: Optional[str] = None
    members_count: Optional[int] = None
    title: Optional[Annotated[str, StringConstraints(max_length=255)]] = None
    description: Optional[Annotated[str, StringConstraints(max_length=255)]] = None
    is_verified: Optional[bool] = None
    is_restricted: Optional[bool] = None
    is_scam: Optional[bool] = None
    is_fake: Optional[bool] = None
    is_forum: Optional[bool] = None
    is_moderated: Optional[bool] = None
    is_closed: Optional[bool] = None

    model_config = SettingsConfigDict(
        from_attributes=True
    )


class ChatAdd(ChatUpdate):
    id: int

    model_config = SettingsConfigDict(
        from_attributes=True
    )
