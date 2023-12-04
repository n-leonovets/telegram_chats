from pydantic import BaseModel


class UserPublic(BaseModel):
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
    is_admin: bool | None = False
    is_disabled: bool | None = False
