import datetime
from typing import Annotated, Union

from fastapi import Query
from pydantic import BaseModel
from pydantic.json_schema import SkipJsonSchema
from sqlalchemy import Select, or_, Update, Delete, and_

from src.models import ChatModel
from src.utils.filters import AbstractFilter


class ChatFilter(BaseModel, AbstractFilter):
    id: int | SkipJsonSchema[None] = None
    username: str | SkipJsonSchema[None] = None
    invite_link: str | SkipJsonSchema[None] = None
    members_count_more: int | SkipJsonSchema[None] = None
    members_count_less: int | SkipJsonSchema[None] = None
    keywords_in_title: Annotated[list[str] | SkipJsonSchema[None], Query(...)] = None
    keywords_in_description: Annotated[list[str] | SkipJsonSchema[None], Query(...)] = None
    is_verified: bool | SkipJsonSchema[None] = None
    is_restricted: bool | SkipJsonSchema[None] = None
    is_scam: bool | SkipJsonSchema[None] = None
    is_fake: bool | SkipJsonSchema[None] = None
    is_forum: bool | SkipJsonSchema[None] = None
    is_moderated: bool | SkipJsonSchema[None] = None
    is_closed: bool | SkipJsonSchema[None] = None
    updated_after: datetime.datetime | SkipJsonSchema[None] = None
    updated_to: datetime.datetime | SkipJsonSchema[None] = None

    def get_conditions(self) -> list:
        filters = self.model_dump(exclude_unset=True)
        conditions = []

        if "id" in filters:
            conditions.append(ChatModel.id == filters["id"])
        if "username" in filters:
            conditions.append(ChatModel.username == filters["username"])
        if "invite_link" in filters:
            conditions.append(ChatModel.invite_link == filters["invite_link"])

        if "members_count_more" in filters:
            conditions.append(ChatModel.members_count > filters["members_count_more"])
        if "members_count_less" in filters:
            conditions.append(ChatModel.members_count < filters["members_count_less"])

        if "keywords_in_title" in filters:
            title_conditions = [
                ChatModel.title.ilike(f"%{search_string}%") for search_string in self.keywords_in_title
            ]
            conditions.append(or_(*title_conditions))

        if "keywords_in_description" in filters:
            description_conditions = [
                ChatModel.title.ilike(f"%{search_string}%") for search_string in self.keywords_in_description
            ]
            conditions.append(or_(*description_conditions))

        if "is_verified" in filters:
            conditions.append(ChatModel.is_verified == filters["is_verified"])
        if "is_restricted" in filters:
            conditions.append(ChatModel.is_restricted == filters["is_restricted"])
        if "is_scam" in filters:
            conditions.append(ChatModel.is_scam == filters["is_scam"])
        if "is_fake" in filters:
            conditions.append(ChatModel.is_fake == filters["is_fake"])
        if "is_forum" in filters:
            conditions.append(ChatModel.is_forum == filters["is_forum"])
        if "is_moderated" in filters:
            conditions.append(ChatModel.is_moderated == filters["is_moderated"])
        if "is_closed" in filters:
            conditions.append(ChatModel.is_closed == filters["is_closed"])

        if "updated_after" in filters:
            conditions.append(ChatModel.updated_at > filters["updated_after"])
        if "updated_to" in filters:
            conditions.append(ChatModel.updated_at < filters["updated_to"])

        return conditions

    def apply(self, query: Union[Select, Update, Delete]) -> Union[Select, Update, Delete]:
        conditions = self.get_conditions()
        return query.where(and_(*conditions))


class ChatListFilter(BaseModel, AbstractFilter):
    filters: list[ChatFilter]

    def apply(self, query: Union[Select, Update, Delete]) -> Union[Select, Update, Delete]:
        conditions = [and_(*f.get_conditions()) for f in self.filters]
        return query.where(or_(*conditions))
