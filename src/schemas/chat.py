import datetime
from typing import Annotated

from pydantic import BaseModel, StringConstraints, field_validator, ValidationError
from pydantic.json_schema import SkipJsonSchema
from pydantic_core import PydanticCustomError
from pydantic_core.core_schema import FieldValidationInfo
from pydantic_settings import SettingsConfigDict


class ChatResponse(BaseModel):
    id: int
    username: str | None = None
    invite_link: str | None = None
    members_count: int
    title: str
    description: str | None = None
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
    username: Annotated[str | SkipJsonSchema[None], StringConstraints(max_length=64)] = None
    invite_link: str | SkipJsonSchema[None] = None
    members_count: int | SkipJsonSchema[None] = None
    title: Annotated[str | SkipJsonSchema[None], StringConstraints(max_length=255)] = None
    description: Annotated[str | SkipJsonSchema[None], StringConstraints(max_length=255)] = None
    is_verified: bool | SkipJsonSchema[None] = None
    is_restricted: bool | SkipJsonSchema[None] = None
    is_scam: bool | SkipJsonSchema[None] = None
    is_fake: bool | SkipJsonSchema[None] = None
    is_forum: bool | SkipJsonSchema[None] = None
    is_moderated: bool | SkipJsonSchema[None] = None
    is_closed: bool | SkipJsonSchema[None] = None

    model_config = SettingsConfigDict(
        from_attributes=True
    )


class ChatAdd(BaseModel):
    id: int
    username: str | SkipJsonSchema[None] = None
    invite_link: str | SkipJsonSchema[None] = None
    members_count: int | SkipJsonSchema[None] = 0
    title: str
    description: str | SkipJsonSchema[None] = None
    is_verified: bool | SkipJsonSchema[None] = False
    is_restricted: bool | SkipJsonSchema[None] = False
    is_scam: bool | SkipJsonSchema[None] = False
    is_fake: bool | SkipJsonSchema[None] = False
    is_forum: bool | SkipJsonSchema[None] = False
    is_moderated: bool | SkipJsonSchema[None] = False
    is_closed: bool | SkipJsonSchema[None] = False

    model_config = SettingsConfigDict(
        from_attributes=True
    )

    @field_validator("username")
    def check_username_and_invite_link_not_empty(cls, username: str, info: FieldValidationInfo):
        invite_link = info.data.get("invite_link")
        if username is None and invite_link is None:
            raise ValueError("username and invite_link can not be both empty")
        return username

    @field_validator("invite_link")
    def check_invite_link_and_username_not_empty(cls, invite_link: str, info: FieldValidationInfo):
        username = info.data.get("username")
        if invite_link is None and username is None:
            raise ValueError("username and invite_link can not be both empty")
        return invite_link
