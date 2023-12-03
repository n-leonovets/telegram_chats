from dataclasses import dataclass

from sqlalchemy import Select

from src.utils.filters import AbstractFilter


@dataclass
class LimitFilter(AbstractFilter):
    limit: int | None = None
    offset: int | None = None

    def apply(self, query: Select) -> Select:
        if self.limit:
            query = query.limit(self.limit)
        if self.offset:
            query = query.offset(self.offset)

        return query
