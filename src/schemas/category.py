import datetime
from typing import Optional

from pydantic import BaseModel

from src.schemas.base import DatetimeBaseModel


class Category(BaseModel):
    name: str
    parent_id: Optional[int] = 0


class CategoryResponse(DatetimeBaseModel):
    id: int
    name: str
    parent_id: int

