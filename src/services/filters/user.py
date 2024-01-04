from typing import Any, Union

from pydantic import BaseModel
from pydantic.json_schema import SkipJsonSchema
from sqlalchemy import Select, Update, Delete, and_, or_

from src.models import UserModel
from src.utils.filters import AbstractFilter


class UserFilter(BaseModel, AbstractFilter):
    username: str | SkipJsonSchema[None] = None
    is_admin: bool | SkipJsonSchema[None] = None
    is_disabled: bool | SkipJsonSchema[None] = None

    def get_conditions(self) -> list:
        filters = self.model_dump(exclude_unset=True)
        conditions = []

        if "username" in filters:
            conditions.append(UserModel.username == filters["username"])
        if "is_admin" in filters:
            conditions.append(UserModel.is_admin == filters["is_admin"])
        if "is_disabled" in filters:
            conditions.append(UserModel.is_disabled == filters["is_disabled"])

        return conditions

    def apply(self, query: Union[Select, Update, Delete]) -> Union[Select, Update, Delete]:
        conditions = self.get_conditions()
        return query.where(and_(*conditions))


class UserListFilter(BaseModel, AbstractFilter):
    filters: list[UserFilter]

    def apply(self, query: Union[Select, Update, Delete]) -> Union[Select, Update, Delete]:
        conditions = [and_(*f.get_conditions()) for f in self.filters]
        return query.where(or_(*conditions))
