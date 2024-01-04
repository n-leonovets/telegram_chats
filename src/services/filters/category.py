from typing import Union

from pydantic import BaseModel
from pydantic.json_schema import SkipJsonSchema
from sqlalchemy import Select, Update, Delete, and_, or_

from src.models import CategoryModel
from src.utils.filters import AbstractFilter


class CategoryFilter(BaseModel, AbstractFilter):
    id: int | SkipJsonSchema[None] = None
    name: str | SkipJsonSchema[None] = None
    parent_id: int | SkipJsonSchema[None] = None

    def get_conditions(self) -> list:
        filters = self.model_dump(exclude_unset=True)
        conditions = []

        if "id" in filters:
            conditions.append(CategoryModel.id == filters["id"])
        if "name" in filters:
            conditions.append(CategoryModel.name == filters["name"])
        if "parent_id" in filters:
            conditions.append(CategoryModel.parent_id == filters["parent_id"])

        return conditions

    def apply(self, query: Union[Select, Update, Delete]) -> Union[Select, Update, Delete]:
        conditions = self.get_conditions()
        return query.where(and_(*conditions))


class CategoryListFilter(BaseModel, AbstractFilter):
    filters: list[CategoryFilter]

    def apply(self, query: Union[Select, Update, Delete]) -> Union[Select, Update, Delete]:
        conditions = [and_(*f.get_conditions()) for f in self.filters]
        return query.where(or_(*conditions))
