from dataclasses import dataclass

from pydantic.json_schema import SkipJsonSchema
from sqlalchemy import Select

from src.models import ChatCategoryModel
from src.utils.filters import AbstractFilter


@dataclass
class ChatCategoryFilter(AbstractFilter):
    chat_id: int | SkipJsonSchema[None] = None
    category_id: int | SkipJsonSchema[None] = None

    def apply(self, query: Select) -> Select:
        if self.chat_id is not None:
            query = query.where(ChatCategoryModel.chat_id == self.chat_id)
        if self.category_id is not None:
            query = query.where(ChatCategoryModel.category_id == self.category_id)

        return query
