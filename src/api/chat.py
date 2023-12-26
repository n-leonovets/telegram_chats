import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.api.auth import required_auth
from src.api.dependencies import UOWDep
from src.schemas.chat import ChatResponse, ChatFullResponse, ChatAdd, ChatUpdate
from src.schemas.user import UserPublic
from src.services.chat import ChatService
from src.services.filters.base import LimitFilter
from src.utils.exception_detail import get_exception_detail
from src.services.filters.chat import ChatDeleteManyFilter, ChatFilter


router = APIRouter(
    prefix="/chats",
    tags=["Chats"]
)
_logger = logging.getLogger(__name__)


@router.post("/")
async def add_chat(
    uow: UOWDep,
    chat: ChatAdd,
    user_auth: UserPublic = Depends(required_auth)
) -> ChatResponse:
    try:
        return await ChatService().add_chat(uow=uow, chat=chat)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router.post("/bulk")
async def add_chats(
    uow: UOWDep,
    chats: list[ChatAdd],
    user_auth: UserPublic = Depends(required_auth)
) -> list[ChatResponse]:
    try:
        return await ChatService().add_chats(uow=uow, chats=chats)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router.get("/")
async def get_chats(
    uow: UOWDep,
    filters: Annotated[ChatFilter, Depends()],
    limits: Annotated[LimitFilter, Depends()],
    user_auth: UserPublic = Depends(required_auth)
) -> list[ChatFullResponse]:
    try:
        return await ChatService().get_chats(uow=uow, filters=filters, limits=limits)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router.patch("/{chat_id}")
async def update_chat(
    uow: UOWDep,
    chat_id: int,
    chat: ChatUpdate,
    user_auth: UserPublic = Depends(required_auth)
) -> ChatResponse:
    try:
        return await ChatService().update_chat(uow=uow, chat=chat, filters=ChatFilter(chat_id=chat_id))
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )
    
@router.patch("/")
async def update_chats(
    uow: UOWDep,
    chat: ChatUpdate,
    filters: Annotated[ChatDeleteManyFilter, Depends()],
    user_auth: UserPublic = Depends(required_auth)
) -> list[ChatResponse]:
    try:
        return await ChatService().update_chats(uow=uow, chat=chat, filters=filters)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )

@router.delete("/")
async def delete_chats(
    uow: UOWDep,
    filters: Annotated[ChatDeleteManyFilter, Depends()],
    user_auth: UserPublic = Depends(required_auth)
) -> None:
    try:
        return await ChatService().delete_chats(uow=uow, filters=filters)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router.delete("/{chat_id}")
async def delete_chat(
    uow: UOWDep,
    chat_id: int,
    user_auth: UserPublic = Depends(required_auth)
) -> ChatResponse:
    try:
        return await ChatService().delete_chat(uow=uow, filters=ChatFilter(chat_id=chat_id))
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )
