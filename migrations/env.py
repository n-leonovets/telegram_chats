import asyncio
import sys

from src_base.database import async_engine, Base


async def init_models() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        print("Таблицы созданы!")


async def main():
    await init_models()


if __name__ == "__main__":
    if sys.platform in ('win32', 'cygwin', 'cli'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        # from winloop import install
        # install()
    else:
        # if we're on apple or linux do this instead
        from uvloop import install
        install()

    asyncio.run(main())
