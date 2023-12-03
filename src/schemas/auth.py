from enum import StrEnum

from pydantic import BaseModel


class Token(BaseModel):
    token: str
    token_type: str


class TokenType(StrEnum):
    token: str
    type: str


class AuthTokens(BaseModel):
    access_token: Token
    refresh_token: Token
