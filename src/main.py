import asyncio
import logging
import sys

from fastapi import FastAPI

from config import settings
from src_base.api.chat import router as chat_router


_logger = logging.getLogger(__name__)


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

app.include_router(chat_router)

origins = [
    "http://localhost:8000",
]


@app.on_event("startup")
async def on_startup():
    if sys.platform in ('win32', 'cygwin', 'cli'):
        # Windows
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    else:
        # Linux & MacOS
        from uvloop import install
        install()


async def shutdown():
    ...
