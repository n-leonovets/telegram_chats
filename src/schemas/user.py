from pydantic import BaseModel
from pydantic.json_schema import SkipJsonSchema

from src.schemas.base import DatetimeBaseModel


class UserPublic(DatetimeBaseModel):
    username: str
    fullname: str
    is_admin: bool | None = False
    is_disabled: bool | None = False


class UserPrivate(UserPublic):
    hashed_password: str


class UserAdd(BaseModel):
    username: str
    fullname: str
    password: str
    is_admin: bool | SkipJsonSchema[None] = False
    is_disabled: bool | SkipJsonSchema[None] = False
