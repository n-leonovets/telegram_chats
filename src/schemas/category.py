import datetime
from typing import Optional

from pydantic import BaseModel


class Category(BaseModel):
    name: str
    parent_id: Optional[int] = 0


class CategoryResponse(BaseModel):
    id: int
    name: str
    parent_id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
