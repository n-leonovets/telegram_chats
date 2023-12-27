import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.api.auth import required_auth
from src.api.dependencies import UOWDep
from src.schemas import Category, CategoryResponse, CategoryFullResponse, UserPublic
from src.services import CategoryService
from src.services.filters import LimitFilter, CategoryFilter
from src.utils.exception_detail import get_exception_detail

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)
_logger = logging.getLogger(__name__)


@router.post("/category/")
async def add_category(
    uow: UOWDep,
    category: Category,
    user_auth: UserPublic = Depends(required_auth)
) -> CategoryResponse:
    try:
        return await CategoryService().add_category(uow=uow, category=category)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router.post("/")
async def add_categories(
    uow: UOWDep,
    categoris: list[Category],
    user_auth: UserPublic = Depends(required_auth)
) -> list[CategoryResponse]:
    try:
        return await CategoryService().add_categoris(uow=uow, categoris=categoris)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router.get("/")
async def get_categories(
    uow: UOWDep,
    filters: Annotated[CategoryFilter, Depends()],
    limits: Annotated[LimitFilter, Depends()],
    user_auth: UserPublic = Depends(required_auth)
) -> list[CategoryFullResponse]:
    try:
        return await CategoryService().get_categories(uow=uow, filters=filters, limits=limits)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router.patch("/{category_id}")
async def update_category(
    uow: UOWDep,
    category_id: int,
    category: Category,
    user_auth: UserPublic = Depends(required_auth)
) -> CategoryResponse:
    try:
        return await CategoryService().update_category(
            uow=uow, category=category, filters=CategoryFilter(id=category_id)
        )
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router.delete("/{category_id}")
async def delete_category(
    uow: UOWDep,
    category_id: int,
    user_auth: UserPublic = Depends(required_auth)
) -> CategoryResponse:
    try:
        return await CategoryService().delete_category(uow=uow, filters=CategoryFilter(id=category_id))
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )
