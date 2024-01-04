import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.api.auth import required_auth
from src.api.dependencies import UOWDep
from src.schemas import ChatResponse, ChatFullResponse, ChatAdd, ChatUpdate
from src.services import ChatService
from src.services.filters import LimitFilter, ChatFilter, ChatListFilter
from src.utils.exception_detail import get_exception_detail


router_secure = APIRouter(
    prefix="/chat",
    tags=["Chat"],
    dependencies=[Depends(required_auth)]
)
_logger = logging.getLogger(__name__)


@router_secure.post("/")
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


@router_secure.get("/")
async def get_chat(
    uow: UOWDep,
    filters: Annotated[ChatFilter, Depends()],
    limits: Annotated[LimitFilter, Depends()]
) -> ChatFullResponse:
    try:
        return await ChatService().get_chat(uow=uow, filters=filters, limits=limits)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.patch("/")
async def update_chat(
    uow: UOWDep,
    chat: ChatUpdate,
    filters: ChatFilter
) -> ChatResponse:
    try:
        return await ChatService().update_chat(uow=uow, chat=chat, filters=filters)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.delete("/")
async def delete_chat(
    uow: UOWDep,
    filters: ChatFilter
) -> ChatResponse:
    try:
        return await ChatService().delete_chat(uow=uow, filters=filters)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.post("/bulk/")
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


@router_secure.get("/bulk/")
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


@router_secure.patch("/bulk/")
async def update_chats(
    uow: UOWDep,
    chats: list[ChatUpdate],
    filters: ChatListFilter
) -> list[ChatResponse]:
    try:
        return await ChatService().update_chats(uow=uow, chats=chats, filters=filters)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.delete("/bulk/")
async def delete_chats(
    uow: UOWDep,
    filters: ChatListFilter
) -> list[ChatResponse]:
    try:
        return await ChatService().delete_chats(uow=uow, filters=filters)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )
