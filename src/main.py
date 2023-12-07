import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from src.api.auth import router as auth_router
from src.api.category import router as category_router
from src.api.chat import router as chat_router
from src.api.chat_category import router as chat_category_router
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
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "*",
        # "Access-Control-Allow-Headers", "Access-Control-Allow-Origin", "Authorization", "Content-Type", "Set-Cookie"
    ],
)

app.include_router(auth_router)
app.include_router(category_router)
app.include_router(chat_router)
app.include_router(chat_category_router)
