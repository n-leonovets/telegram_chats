import datetime
from typing import Optional, Annotated

from pydantic import BaseModel, StringConstraints, validator
from pydantic.json_schema import SkipJsonSchema
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
    title: str | SkipJsonSchema[None] = None
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

    @validator("title", pre=True, always=True)
    @classmethod
    def check_attr1_and_attr2_not_empty(cls, value, values):
        attr2_value = values.get("description")
        if value is None and attr2_value is None:
            raise ValueError("title and description cannot be both empty")
        return value

    @validator("description", pre=True, always=True)
    @classmethod
    def check_attr2_and_attr1_not_empty(cls, value, values):
        attr1_value = values.get("title")
        if value is None and attr1_value is None:
            raise ValueError("title and description cannot be both empty")
        return value
