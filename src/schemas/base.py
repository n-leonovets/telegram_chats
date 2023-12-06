import datetime

from pydantic import BaseModel


class DatetimeBaseModel(BaseModel):
    created_at: datetime.datetime
    updated_at: datetime.datetime
