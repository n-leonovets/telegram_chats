import datetime
from typing import Annotated

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base, str32, str255


updated_at = Annotated[datetime.datetime, mapped_column(
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp
    )]


class ChatTable(Base):
    __tablename__ = "chat"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=False)
    username: Mapped[str32 | None]
    invite_link: Mapped[str255 | None]
    members_count: Mapped[int] = mapped_column(server_default="0")
    title: Mapped[str255]
    description: Mapped[str255 | None]
    is_verified: Mapped[bool] = mapped_column(server_default="false")
    is_restricted: Mapped[bool] = mapped_column(server_default="false")
    is_scam: Mapped[bool] = mapped_column(server_default="false")
    is_fake: Mapped[bool] = mapped_column(server_default="false")
    is_forum: Mapped[bool] = mapped_column(server_default="false")
    is_moderated: Mapped[bool] = mapped_column(server_default="false")
    is_closed: Mapped[bool] = mapped_column(server_default="false")
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp
    )
