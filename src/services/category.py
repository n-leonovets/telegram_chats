from typing import Optional

from src.models.category import CategoryModel
from src.schemas.category import CategoryResponse, Category
from src.services.filters.base import LimitFilter
from src.services.filters.category import CategoryFilter
from src.utils.unitofwork import AbstractUnitOfWork


class CategoryService:
    @staticmethod
    async def add_category(uow: AbstractUnitOfWork, category: Category) -> CategoryResponse:
        async with uow:
            result: CategoryModel = await uow.category.create_one(values=category.model_dump())
            await uow.commit()
            return CategoryResponse(**result.__dict__)

    @staticmethod
    async def add_categoris(uow: AbstractUnitOfWork, categoris: list[Category]) -> list[CategoryResponse]:
        async with uow:
            result: list[CategoryModel] = await uow.category.create_all(
                values=[category.model_dump() for category in categoris]
            )
            await uow.commit()
            return [CategoryResponse(**category.__dict__) for category in result]

    @staticmethod
    async def get_categories(
        uow: AbstractUnitOfWork,
        filters: Optional[CategoryFilter] = None,
        limits: Optional[LimitFilter] = None
    ) -> list[CategoryResponse]:
        async with uow:
            result: list[CategoryModel] = await uow.category.read_all(filters=filters, limits=limits)
            return [CategoryResponse(**category.__dict__) for category in result]

    @staticmethod
    async def get_category(uow: AbstractUnitOfWork, filters: CategoryFilter) -> CategoryResponse:
        async with uow:
            result: CategoryModel = await uow.category.read_one(filters=filters)
            return CategoryResponse(**result.__dict__)

    @staticmethod
    async def update_category(uow: AbstractUnitOfWork, category: Category, filters: CategoryFilter) -> CategoryResponse:
        async with uow:
            result: CategoryModel = await uow.category.update_one(
                values=category.model_dump(exclude_none=True),
                filters=filters
            )
            await uow.commit()
            return CategoryResponse(**result.__dict__)

    @staticmethod
    async def delete_category(uow: AbstractUnitOfWork, filters: CategoryFilter) -> CategoryResponse:
        async with uow:
            result: CategoryModel = await uow.category.delete_one(filters=filters)
            await uow.commit()
            return CategoryResponse(**result.__dict__)
