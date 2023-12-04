from typing import Optional

from pydantic import BaseModel


class CategoryInSchema(BaseModel):
    name: str
    parent_id: Optional[int] = 0


class CategoryOutSchema(CategoryInSchema):
    id: int
