import logging
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.api.auth import required_auth
from src.api.dependencies import UOWDep
from src.schemas import Category, CategoryResponse, CategoryFullResponse
from src.services import CategoryService
from src.services.filters import LimitFilter, CategoryFilter
from src.utils.exception_detail import get_exception_detail


router_secure = APIRouter(
    prefix="/categories",
    tags=["Categories"],
    dependencies=[Depends(required_auth)]
)

_logger = logging.getLogger(__name__)


@router_secure.post("/category/")
async def add_category(
    uow: UOWDep,
    category: Category
) -> CategoryResponse:
    try:
        return await CategoryService().add_category(uow=uow, category=category)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.post("/")
async def add_categories(
    uow: UOWDep,
    categoris: list[Category]
) -> list[CategoryResponse]:
    try:
        return await CategoryService().add_categoris(uow=uow, categoris=categoris)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.get("/")
async def get_categories(
    uow: UOWDep,
    filters: Annotated[CategoryFilter, Depends()],
    limits: Annotated[LimitFilter, Depends()]
) -> list[CategoryFullResponse]:
    try:
        return await CategoryService().get_categories(uow=uow, filters=filters, limits=limits)
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )


@router_secure.patch("/{category_id}")
async def update_category(
    uow: UOWDep,
    category_id: int,
    category: Category
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


@router_secure.delete("/{category_id}")
async def delete_category(
    uow: UOWDep,
    category_id: int
) -> CategoryResponse:
    try:
        return await CategoryService().delete_category(uow=uow, filters=CategoryFilter(id=category_id))
    except Exception as e:
        _logger.error("Exception error", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=get_exception_detail(e)
        )
