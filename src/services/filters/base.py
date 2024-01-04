from pydantic import BaseModel
from pydantic.json_schema import SkipJsonSchema
from sqlalchemy import Select

from src.utils.filters import AbstractFilter


class LimitFilter(AbstractFilter, BaseModel):
    limit: int | SkipJsonSchema[None] = None
    offset: int | SkipJsonSchema[None] = None

    def apply(self, query: Select) -> Select:
        if self.limit is not None:
            query = query.limit(self.limit)
        if self.offset is not None:
            query = query.offset(self.offset)

        return query
