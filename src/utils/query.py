import datetime
from dataclasses import dataclass
from abc import abstractmethod, ABC
from typing import Annotated, Any

from fastapi import Query
from pydantic.json_schema import SkipJsonSchema
from sqlalchemy import Select, or_

from src.models.chat import ChatTable


@dataclass
class AbstractFilter(ABC):
    @abstractmethod
    def apply(self, query: Any) -> Select:
        pass


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


@dataclass
class ChatFilter(AbstractFilter):
    chat_id: int | SkipJsonSchema[None] = None
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

    def apply(self, query: Select) -> Select:
        if self.chat_id is not None:
            query = query.where(ChatTable.id == self.chat_id)
        if self.username is not None:
            query = query.where(ChatTable.username == self.username)
        if self.invite_link is not None:
            query = query.where(ChatTable.invite_link == self.invite_link)

        if self.members_count_more is not None:
            query = query.where(ChatTable.members_count > self.members_count_more)
        if self.members_count_less is not None:
            query = query.where(ChatTable.members_count < self.members_count_less)

        if self.keywords_in_title:
            title_conditions = [
                ChatTable.title.ilike(f"%{search_string}%") for search_string in self.keywords_in_title
            ]
            query = query.where(or_(*title_conditions))

        if self.keywords_in_description:
            description_conditions = [
                ChatTable.title.ilike(f"%{search_string}%") for search_string in self.keywords_in_description
            ]
            query = query.where(or_(*description_conditions))

        if self.is_verified is not None:
            query = query.where(ChatTable.is_verified == self.is_verified)
        if self.is_restricted is not None:
            query = query.where(ChatTable.is_restricted == self.is_restricted)
        if self.is_scam is not None:
            query = query.where(ChatTable.is_scam == self.is_scam)
        if self.is_fake is not None:
            query = query.where(ChatTable.is_fake == self.is_fake)
        if self.is_forum is not None:
            query = query.where(ChatTable.is_forum == self.is_forum)
        if self.is_moderated is not None:
            query = query.where(ChatTable.is_moderated == self.is_moderated)
        if self.is_closed is not None:
            query = query.where(ChatTable.is_closed == self.is_closed)

        if self.updated_after is not None:
            query = query.where(ChatTable.updated_at > self.updated_after)
        if self.updated_to is not None:
            query = query.where(ChatTable.updated_at < self.updated_to)

        return query
