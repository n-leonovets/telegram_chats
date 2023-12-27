import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.api.auth import required_auth
from src.api.dependencies import UOWDep
from src.schemas import ChatCategory, ChatCategoryResponse, UserPublic
from src.services import ChatCategoryService
from src.services.filters import LimitFilter, ChatCategoryFilter
from src.utils.exception_detail import get_exception_detail

router = APIRouter(
    prefix="/chat_categories",
    tags=["Chat Categories"]
)
_logger = logging.getLogger(__name__)


@router.post("/chat_category/")
async def add_chat_category(
    uow: UOWDep,
    chat_category: ChatCategory,
    user_auth: UserPublic = Depends(required_auth)
) -> ChatCategoryResponse:
    try:
        return await ChatCategoryService().add_chat_category(uow=uow, chat_category=chat_category)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router.post("/")
async def add_chat_categories(
    uow: UOWDep,
    chat_categories: list[ChatCategory],
    user_auth: UserPublic = Depends(required_auth)
) -> list[ChatCategoryResponse]:
    try:
        return await ChatCategoryService().add_chat_categories(uow=uow, chat_categories=chat_categories)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router.get("/")
async def get_chat_categories(
    uow: UOWDep,
    filters: Annotated[ChatCategoryFilter, Depends()],
    limits: Annotated[LimitFilter, Depends()],
    user_auth: UserPublic = Depends(required_auth)
) -> list[ChatCategoryResponse]:
    try:
        return await ChatCategoryService().get_chat_categories(uow=uow, filters=filters, limits=limits)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router.patch("/{chat_id}/{category_id}")
async def update_chat_category(
    uow: UOWDep,
    chat_id: int,
    category_id: int,
    user_auth: UserPublic = Depends(required_auth)
) -> ChatCategoryResponse:
    try:
        return await ChatCategoryService().update_chat_category(
            uow=uow,
            chat_category=ChatCategory(
                chat_id=chat_id,
                category_id=category_id
            ),
            filters=ChatCategoryFilter(
                chat_id=chat_id,
                category_id=category_id
            )
        )
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router.delete("/{chat_id}/{category_id}")
async def delete_category(
    uow: UOWDep,
    chat_id: int,
    category_id: int,
    user_auth: UserPublic = Depends(required_auth)
) -> ChatCategoryResponse:
    try:
        return await ChatCategoryService().delete_chat_category(
            uow=uow,
            filters=ChatCategoryFilter(
                chat_id=chat_id,
                category_id=category_id
            )
        )
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )
