from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    fullname: str
    is_admin: bool | None = False
    is_disabled: bool | None = False


class UserIDBSchema(UserSchema):
    hashed_password: str


class UserInSchema(BaseModel):
    username: str
    fullname: str
    is_admin: bool | None = False
    is_disabled: bool | None = False


class UserOutSchema(UserInSchema):
    hashed_password: str
