import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.api.dependencies import UOWDep
from src.schemas.chat import ChatSchema, ChatAddSchema, ChatUpdateSchema
from src.services.chat import ChatService
from src.utils.api_response import ApiResponse, ApiErrorDetail
from src.utils.query import ChatFilter, LimitFilter

router = APIRouter(
    prefix="/chats",
    tags=["Chats"]
)
_logger = logging.getLogger(__name__)


@router.post("/chat/")
async def add_chat(
    chat: ChatAddSchema,
    uow: UOWDep
) -> ApiResponse[ChatSchema]:
    try:
        result = await ChatService().add_chat(uow=uow, chat=chat)
        return ApiResponse(
            status_code=status.HTTP_201_CREATED,
            data=result
        )
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
    chats: list[ChatAddSchema],
    uow: UOWDep
) -> ApiResponse[list[ChatSchema]]:
    try:
        result = await ChatService().add_chats(uow=uow, chats=chats)
        return ApiResponse(
            status_code=status.HTTP_201_CREATED,
            data=result
        )
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
    filters: Annotated[ChatFilter, Depends()],
    limits: Annotated[LimitFilter, Depends()],
    uow: UOWDep
) -> ApiResponse[list[ChatSchema]]:
    try:
        result = await ChatService().get_chats(uow=uow, filters=filters, limits=limits)
        return ApiResponse(
            status_code=status.HTTP_200_OK,
            data=result
        )
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
    chat_id: int,
    chat: Annotated[ChatUpdateSchema, Depends()],
    uow: UOWDep
) -> ApiResponse[ChatSchema]:
    try:
        result = await ChatService().update_chat(uow=uow, chat=chat, filter_by={"id": chat_id})
        return ApiResponse(
            status_code=status.HTTP_200_OK,
            data=result
        )
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
    chat_id: int,
    uow: UOWDep
) -> ApiResponse[ChatSchema]:
    try:
        result = await ChatService().delete_chat(uow=uow, filter_by={"id": chat_id})
        return ApiResponse(
            status_code=status.HTTP_200_OK,
            data=result
        )
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
