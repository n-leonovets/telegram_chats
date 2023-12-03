from enum import StrEnum, auto

from pydantic import BaseModel


class TokenType(StrEnum):
    ACCESS = auto()
    REFRESH = auto()


class Token(BaseModel):
    token: str
    type: TokenType
    token_type: str


class AuthTokens(BaseModel):
    access_token: Token
    refresh_token: Token
