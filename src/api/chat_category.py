import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.api.auth import required_auth
from src.api.dependencies import UOWDep
from src.schemas import ChatCategory, ChatCategoryResponse
from src.services import ChatCategoryService
from src.services.filters import LimitFilter, ChatCategoryFilter, ChatCategoryListFilter
from src.utils.exception_detail import get_exception_detail

router_secure = APIRouter(
    prefix="/chat_category",
    tags=["Chat Category"],
    dependencies=[Depends(required_auth)]
)
_logger = logging.getLogger(__name__)


@router_secure.post("/")
async def add_chat_category(
    uow: UOWDep,
    chat_category: ChatCategory
) -> ChatCategoryResponse:
    try:
        return await ChatCategoryService().add_chat_category(uow=uow, chat_category=chat_category)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.get("/")
async def get_chat_category(
    uow: UOWDep,
    filters: Annotated[ChatCategoryFilter, Depends()]
) -> ChatCategoryResponse:
    try:
        return await ChatCategoryService().get_chat_category(uow=uow, filters=filters)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.patch("/")
async def update_chat_category(
    uow: UOWDep,
    chat_category: ChatCategory,
    filters: ChatCategoryFilter
) -> ChatCategoryResponse:
    try:
        return await ChatCategoryService().update_chat_category(
            uow=uow,
            chat_category=chat_category,
            filters=filters
        )
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.delete("/")
async def delete_chat_category(
    uow: UOWDep,
    filters: ChatCategoryFilter
) -> ChatCategoryResponse:
    try:
        return await ChatCategoryService().delete_chat_category(
            uow=uow,
            filters=filters
        )
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.post("/bulk/")
async def add_chats_categories(
    uow: UOWDep,
    chat_categories: list[ChatCategory]
) -> list[ChatCategoryResponse]:
    try:
        return await ChatCategoryService().add_chats_categories(uow=uow, chat_categories=chat_categories)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.get("/bulk/")
async def get_chats_categories(
    uow: UOWDep,
    filters: Annotated[ChatCategoryFilter, Depends()],
    limits: Annotated[LimitFilter, Depends()]
) -> list[ChatCategoryResponse]:
    try:
        return await ChatCategoryService().get_chats_categories(uow=uow, filters=filters, limits=limits)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.patch("/bulk/")
async def update_chats_categories(
    uow: UOWDep,
    chats_categories: list[ChatCategory],
    filters: ChatCategoryListFilter
) -> list[ChatCategoryResponse]:
    try:
        return await ChatCategoryService().update_chats_categories(
            uow=uow,
            chats_categories=chats_categories,
            filters=filters
        )
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.delete("/bulk/")
async def delete_chats_categories(
    uow: UOWDep,
    filters: ChatCategoryListFilter
) -> list[ChatCategoryResponse]:
    try:
        return await ChatCategoryService().delete_chats_categories(uow=uow, filters=filters)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )
