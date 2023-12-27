from dataclasses import dataclass
from typing import Any, Union

from pydantic.json_schema import SkipJsonSchema
from sqlalchemy import Select, Update, Delete

from src.models import UserModel
from src.utils.filters import AbstractFilter


@dataclass
class UserFilter(AbstractFilter):
    username: str | SkipJsonSchema[None] = None
    is_admin: bool | SkipJsonSchema[None] = None
    is_disabled: bool | SkipJsonSchema[None] = None

    def apply(self, query: Any) -> Union[Select, Update, Delete]:
        if self.username is not None:
            query = query.where(UserModel.username == self.username)
        if self.is_admin is not None:
            query = query.where(UserModel.is_admin == self.is_admin)
        if self.is_disabled is not None:
            query = query.where(UserModel.is_disabled == self.is_disabled)

        return query
