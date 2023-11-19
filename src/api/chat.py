import logging
from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import chat_service
from src.schemas.chat import ChatModel
from src.services.chat import ChatService
from src.utils.api_response import ApiResponse, ApiError
from src.utils.query import ChatFilter, LimitFilter

router = APIRouter(
    prefix="/chats",
    tags=["Chats"]
)
_logger = logging.getLogger(__name__)


@router.get("/")
async def get_chats(
    filters: Annotated[ChatFilter, Depends()],
    limits: Annotated[LimitFilter, Depends()],
    chat_serivece: Annotated[ChatService, Depends(chat_service)]
) -> ApiResponse[list[ChatModel]]:
    try:
        chats = await chat_serivece.get_chats(filters=filters, limits=limits)
        return ApiResponse(
            status_code=200,
            data=chats
        )
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        return ApiResponse(
            status_code=500,
            details=ApiError(
                module=e.__class__.__module__,
                name=e.__class__.__name__,
                message=e.args[0]
            )
        )


@router.post("/")
async def add_chat(
    chat: ChatModel,
    chat_serivece: Annotated[ChatService, Depends(chat_service)]
) -> ApiResponse[ChatModel]:
    try:
        chat = chat_serivece.add_chat(chat)
        return ApiResponse(
            status_code=200,
            data=chat
        )
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        return ApiResponse(
            status_code=500,
            details=ApiError(
                module=e.__class__.__module__,
                name=e.__class__.__name__,
                message=e.args[0]
            )
        )
