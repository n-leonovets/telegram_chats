import logging

from fastapi import FastAPI

from config import settings
from src.api.auth import router as auth_router
from src.api.category import router as category_router
from src.api.chat import router as chat_router
from src.middleware import LogStatsMiddleware
from src.utils.asyncio_utils import asyncio_speedup

_logger = logging.getLogger(__name__)


async def on_startup():
    asyncio_speedup()


async def on_shutdown():
    ...


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    on_startup=[on_startup],
    on_shutdown=[on_shutdown]
)

origins = [
    "http://localhost:8000",
]

app.add_middleware(LogStatsMiddleware)

app.include_router(auth_router)
app.include_router(category_router)
app.include_router(chat_router)


