from typing import Optional

from src.models import CategoryModel
from src.schemas import CategoryResponse, CategoryFullResponse, Category
from src.services.filters import LimitFilter, CategoryFilter, CategoryListFilter
from src.utils.unitofwork import AbstractUnitOfWork


class CategoryService:
    @staticmethod
    async def add_category(
        uow: AbstractUnitOfWork,
        category: Category
    ) -> CategoryResponse:
        async with uow:
            result: CategoryModel = await uow.category.create_one(values=category.model_dump())
            await uow.commit()
            return CategoryResponse.model_validate(result, from_attributes=True)

    @staticmethod
    async def get_category(
        uow: AbstractUnitOfWork,
        filters: CategoryFilter
    ) -> CategoryFullResponse:
        async with uow:
            result: CategoryModel = await uow.category.read_one(filters=filters)
            return CategoryFullResponse.model_validate(result, from_attributes=True)

    @staticmethod
    async def update_category(
        uow: AbstractUnitOfWork,
        category: Category,
        filters: CategoryFilter
    ) -> CategoryResponse:
        async with uow:
            result: CategoryModel = await uow.category.update_one(
                values=category.model_dump(exclude_unset=True),
                filters=filters
            )
            await uow.commit()
            return CategoryResponse.model_validate(result, from_attributes=True)

    @staticmethod
    async def delete_category(
        uow: AbstractUnitOfWork,
        filters: CategoryFilter
    ) -> CategoryResponse:
        async with uow:
            result: CategoryModel = await uow.category.delete_one(filters=filters)
            await uow.commit()
            return CategoryResponse.model_validate(result, from_attributes=True)

    @staticmethod
    async def add_categories(
        uow: AbstractUnitOfWork,
        categories: list[Category]
    ) -> list[CategoryResponse]:
        async with uow:
            result: list[CategoryModel] = await uow.category.create_many(
                values=[category.model_dump() for category in categories]
            )
            await uow.commit()
            return [
                CategoryResponse.model_validate(
                    row,
                    from_attributes=True
                ) for row in result
            ]

    @staticmethod
    async def get_categories(
        uow: AbstractUnitOfWork,
        filters: Optional[CategoryFilter] = None,
        limits: Optional[LimitFilter] = None
    ) -> list[CategoryFullResponse]:
        async with uow:
            result: list[CategoryModel] = await uow.category.read_many(filters=filters, limits=limits)
            return [
                CategoryFullResponse.model_validate(
                    row,
                    from_attributes=True)
                for row in result
            ]

    @staticmethod
    async def update_categories(
        uow: AbstractUnitOfWork,
        categories: list[Category],
        filters: CategoryListFilter
    ) -> list[CategoryResponse]:
        async with uow:
            result: list[CategoryModel] = await uow.category.update_many(
                values=[
                    category.model_dump(exclude_unset=True)
                    for category in categories
                ],
                filters=filters
            )
            await uow.commit()
            return [
                CategoryResponse.model_validate(
                    category,
                    from_attributes=True
                ) for category in result
            ]

    @staticmethod
    async def delete_categories(
        uow: AbstractUnitOfWork,
        filters: CategoryListFilter
    ) -> list[CategoryResponse]:
        async with uow:
            result: list[CategoryModel] = await uow.category.delete_many(filters=filters)
            await uow.commit()
            return [
                CategoryResponse.model_validate(
                    category,
                    from_attributes=True
                ) for category in result
            ]
