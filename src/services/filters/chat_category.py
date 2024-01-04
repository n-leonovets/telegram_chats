from typing import Union

from pydantic import BaseModel
from pydantic.json_schema import SkipJsonSchema
from sqlalchemy import Select, Update, Delete, and_, or_

from src.models import ChatCategoryModel
from src.utils.filters import AbstractFilter


class ChatCategoryFilter(BaseModel, AbstractFilter):
    chat_id: int | SkipJsonSchema[None] = None
    category_id: int | SkipJsonSchema[None] = None

    def get_conditions(self) -> list:
        filters = self.model_dump(exclude_unset=True)
        conditions = []

        if "chat_id" in filters:
            conditions.append(ChatCategoryModel.chat_id == filters["chat_id"])
        if "category_id" in filters:
            conditions.append(ChatCategoryModel.category_id == filters["category_id"])

        return conditions

    def apply(self, query: Union[Select, Update, Delete]) -> Union[Select, Update, Delete]:
        conditions = self.get_conditions()
        return query.where(and_(*conditions))


class ChatCategoryListFilter(BaseModel, AbstractFilter):
    filters: list[ChatCategoryFilter]

    def apply(self, query: Union[Select, Update, Delete]) -> Union[Select, Update, Delete]:
        conditions = [and_(*f.get_conditions()) for f in self.filters]
        return query.where(or_(*conditions))
