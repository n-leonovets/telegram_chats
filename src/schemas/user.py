import datetime

from pydantic import BaseModel
from pydantic.json_schema import SkipJsonSchema


class UserPublic(BaseModel):
    username: str
    fullname: str
    is_admin: bool | None = False
    is_disabled: bool | None = False
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserPrivate(UserPublic):
    hashed_password: str


class UserAdd(BaseModel):
    username: str
    fullname: str
    password: str
    is_admin: bool | SkipJsonSchema[None] = False
    is_disabled: bool | SkipJsonSchema[None] = False
