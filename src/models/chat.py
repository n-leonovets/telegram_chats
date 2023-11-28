import datetime
from typing import Annotated

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base, str32, str255, updated_at

boolFalse = Annotated[bool, mapped_column(server_default="false")]


class ChatTable(Base):
    __tablename__ = "chat"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    username: Mapped[str32 | None]
    invite_link: Mapped[str255 | None]
    members_count: Mapped[int] = mapped_column(server_default="0")
    title: Mapped[str255]
    description: Mapped[str255 | None]
    is_verified: Mapped[boolFalse]
    is_restricted: Mapped[boolFalse]
    is_scam: Mapped[boolFalse]
    is_fake: Mapped[boolFalse]
    is_forum: Mapped[boolFalse]
    is_moderated: Mapped[boolFalse]
    is_closed: Mapped[boolFalse]
    updated_at: Mapped[updated_at]
