import asyncio

from src.database import async_engine, Base
from src.models import chat, category, chat_category, user

from src.schemas.user import UserPrivate
from src.services.user import UserService
from src.utils.asyncio_utils import asyncio_speedup
from src.utils.unitofwork import UnitOfWork

from config import settings


async def init_models() -> None:
    try:
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

        await UserService.add_user(
            uow=UnitOfWork(),
            user=UserPrivate(
                username=settings.ADMIN_USERNAME,
                fullname="First Admin User",
                hashed_password=settings.ADMIN_HASHED_PASSWORD,
                is_admin=True
            )
        )
        print("Таблицы созданы!")
    except Exception as e:
        print(e)


async def main():
    await init_models()


if __name__ == "__main__":
    asyncio_speedup()
    asyncio.run(main())

