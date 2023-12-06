import asyncio
import logging
import sys

import uvloop
from fastapi import FastAPI

from config import settings
from src.api.auth import router as auth_router
from src.api.category import router as category_router
from src.api.chat import router as chat_router
from src.utils.asyncio_utils import asyncio_speedup

_logger = logging.getLogger(__name__)


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

app.include_router(auth_router)
app.include_router(category_router)
app.include_router(chat_router)

origins = [
    "http://localhost:8000",
]


@app.on_event("startup")
async def on_startup():
    asyncio_speedup()


async def shutdown():
    ...
