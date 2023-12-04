from dataclasses import dataclass

from pydantic.json_schema import SkipJsonSchema
from sqlalchemy import Select

from src.models.category import CategoryModel
from src.utils.filters import AbstractFilter


@dataclass
class CategoryFilter(AbstractFilter):
    id: int | SkipJsonSchema[None] = None
    name: str | SkipJsonSchema[None] = None
    parent_id: int | SkipJsonSchema[None] = None

    def apply(self, query: Select) -> Select:
        if self.id is not None:
            query = query.where(CategoryModel.id == self.id)
        if self.name is not None:
            query = query.where(CategoryModel.name == self.name)
        if self.parent_id is not None:
            query = query.where(CategoryModel.parent_id == self.parent_id)

        return query
