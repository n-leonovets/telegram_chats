import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.api.auth import required_auth
from src.api.dependencies import UOWDep
from src.schemas.chat import ChatSchema, ChatAddSchema, ChatUpdateSchema
from src.schemas.user import UserIDBSchema
from src.services.chat import ChatService
from src.services.filters.base import LimitFilter
from src.utils.api_response import ApiErrorDetail
from src.services.filters.chat import ChatFilter

router = APIRouter(
    prefix="/chats",
    tags=["Chats"]
)
_logger = logging.getLogger(__name__)


@router.post("/chat/")
async def add_chat(
    uow: UOWDep,
    chat: ChatAddSchema,
    user_auth: UserIDBSchema = Depends(required_auth)
) -> ChatSchema:
    try:
        return await ChatService().add_chat(uow=uow, chat=chat)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        detail = ApiErrorDetail(
            module=e.__class__.__module__,
            name=e.__class__.__name__,
            message=e.args[0]
        ).model_dump()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={**detail}
        )


@router.post("/")
async def add_chats(
    uow: UOWDep,
    chats: list[ChatAddSchema],
    user_auth: UserIDBSchema = Depends(required_auth)
) -> list[ChatSchema]:
    try:
        return await ChatService().add_chats(uow=uow, chats=chats)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        detail = ApiErrorDetail(
            module=e.__class__.__module__,
            name=e.__class__.__name__,
            message=e.args[0]
        ).model_dump()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={**detail}
        )


@router.get("/")
async def get_chats(
    uow: UOWDep,
    filters: Annotated[ChatFilter, Depends()],
    limits: Annotated[LimitFilter, Depends()],
    user_auth: UserIDBSchema = Depends(required_auth)
) -> list[ChatSchema]:
    try:
        return await ChatService().get_chats(uow=uow, filters=filters, limits=limits)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        detail = ApiErrorDetail(
            module=e.__class__.__module__,
            name=e.__class__.__name__,
            message=e.args[0]
        ).model_dump()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={**detail}
        )


@router.patch("/{chat_id}")
async def update_chat(
    uow: UOWDep,
    chat_id: int,
    chat: Annotated[ChatUpdateSchema, Depends()],
    user_auth: UserIDBSchema = Depends(required_auth)
) -> ChatSchema:
    try:
        return await ChatService().update_chat(uow=uow, chat=chat, filter_by={"id": chat_id})
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        detail = ApiErrorDetail(
            module=e.__class__.__module__,
            name=e.__class__.__name__,
            message=e.args[0]
        ).model_dump()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={**detail}
        )


@router.delete("/{chat_id}")
async def delete_chat(
    uow: UOWDep,
    chat_id: int,
    user_auth: UserIDBSchema = Depends(required_auth)
) -> ChatSchema:
    try:
        return await ChatService().delete_chat(uow=uow, filter_by={"id": chat_id})
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        detail = ApiErrorDetail(
            module=e.__class__.__module__,
            name=e.__class__.__name__,
            message=e.args[0]
        ).model_dump()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={**detail}
        )
