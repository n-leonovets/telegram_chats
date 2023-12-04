from enum import StrEnum, auto

from pydantic import BaseModel


class TokenType(StrEnum):
    ACCESS = auto()
    REFRESH = auto()


class TokensResponse(BaseModel):
    access_token: str
    refresh_token: str
    type: str = "bearer"
