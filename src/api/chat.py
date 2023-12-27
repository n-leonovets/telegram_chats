import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.api.auth import required_auth
from src.api.dependencies import UOWDep
from src.schemas import ChatResponse, ChatFullResponse, ChatAdd, ChatUpdate
from src.services import ChatService
from src.services.filters import LimitFilter, ChatFilter
from src.utils.exception_detail import get_exception_detail


router_secure = APIRouter(
    prefix="/chats",
    tags=["Chats"],
    dependencies=[Depends(required_auth)]
)
_logger = logging.getLogger(__name__)


@router_secure.post("/chat/")
async def add_chat(
    uow: UOWDep,
    chat: ChatAdd
) -> ChatResponse:
    try:
        return await ChatService().add_chat(uow=uow, chat=chat)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.post("/")
async def add_chats(
    uow: UOWDep,
    chats: list[ChatAdd]
) -> list[ChatResponse]:
    try:
        return await ChatService().add_chats(uow=uow, chats=chats)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.get("/")
async def get_chats(
    uow: UOWDep,
    filters: Annotated[ChatFilter, Depends()],
    limits: Annotated[LimitFilter, Depends()]
) -> list[ChatFullResponse]:
    try:
        return await ChatService().get_chats(uow=uow, filters=filters, limits=limits)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.patch("/{chat_id}")
async def update_chat(
    uow: UOWDep,
    chat_id: int,
    chat: ChatUpdate
) -> ChatResponse:
    try:
        return await ChatService().update_chat(uow=uow, chat=chat, filters=ChatFilter(chat_id=chat_id))
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.delete("/{chat_id}")
async def delete_chat(
    uow: UOWDep,
    chat_id: int
) -> ChatResponse:
    try:
        return await ChatService().delete_chat(uow=uow, filters=ChatFilter(chat_id=chat_id))
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )
