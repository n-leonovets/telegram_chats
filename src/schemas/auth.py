from enum import StrEnum, auto

from pydantic import BaseModel


class TokenType(StrEnum):
    ACCESS = auto()
    REFRESH = auto()


class AuthTokens(BaseModel):
    access_token: str
    refresh_token: str
    type: str = "bearer"
