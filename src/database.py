import datetime
from typing import AsyncGenerator, Annotated

from fastapi import HTTPException
from sqlalchemy import String, func, TIMESTAMP, BIGINT
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

from config import settings


async_engine = create_async_engine(
    url=settings.get_asyncpg_url,
    echo=True if settings.DEBUG is True else False,
    pool_size=10,
    max_overflow=100,
    connect_args={
        "server_settings": {
            "application_name": "Telegram Chats"
        }
    }
)

async_session_maker = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
        except (Exception, HTTPException):
            await session.rollback()
            raise
        else:
            await session.commit()
        finally:
            await session.close()


bigint = Annotated[int, int]
str32 = Annotated[str, 32]
str64 = Annotated[str, 64]
str255 = Annotated[str, 255]
boolFalse = Annotated[bool, mapped_column(server_default="false")]
created_at = Annotated[datetime.datetime, mapped_column(
        server_default=func.current_timestamp()
    )]
updated_at = Annotated[datetime.datetime, mapped_column(
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp()
    )]


class Base(DeclarativeBase):
    type_annotation_map = {
        bigint: BIGINT,
        str32: String(32),
        str64: String(64),
        str255: String(255),
        datetime.datetime: TIMESTAMP(timezone=False),
    }
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
