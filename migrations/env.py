import asyncio
import sys

from src.database import async_engine, Base
from src.models import chat, chat_category, user


async def init_models() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print("Таблицы созданы!")


async def main():
    await init_models()


if __name__ == "__main__":
    if sys.platform in ('win32', 'cygwin', 'cli'):
        # Windows
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    else:
        # Linux & MacOS
        from uvloop import install
        install()

    asyncio.run(main())
    # python -m migrations.env

