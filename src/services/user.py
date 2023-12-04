from typing import Optional

from src.models.user import UserModel
from src.schemas.user import UserIDBSchema
from src.services.filters.base import LimitFilter
from src.services.filters.user import UserFilter
from src.utils.unitofwork import AbstractUnitOfWork


class UserService:
    @staticmethod
    async def add_user(
        uow: AbstractUnitOfWork,
        user: UserIDBSchema
    ) -> UserIDBSchema:
        async with uow:
            result: UserModel = await uow.user.create_one(values=user.model_dump())
            await uow.commit()
            return UserIDBSchema(**result.__dict__)

    @staticmethod
    async def get_user(
        uow: AbstractUnitOfWork,
        filters: Optional[UserFilter] = None
    ) -> UserIDBSchema:
        async with uow:
            result: UserModel = await uow.user.read_one(filters=filters)
            return UserIDBSchema(**result.__dict__)

    @staticmethod
    async def get_users(
        uow: AbstractUnitOfWork,
        filters: Optional[UserFilter] = None,
        limits: Optional[LimitFilter] = None
    ) -> list[UserIDBSchema]:
        async with uow:
            result: list[UserModel] = await uow.user.read_all(filters=filters, limits=limits)
            return [UserIDBSchema(**user.__dict__) for user in result]

    @staticmethod
    async def update_user(
        uow: AbstractUnitOfWork,
        user: UserIDBSchema,
        filters: Optional[UserFilter] = None
    ) -> UserIDBSchema:
        async with uow:
            result: UserModel = await uow.user.update_one(
                values=user.model_dump(),
                filters=filters
            )
            return UserIDBSchema(**result.__dict__)

    @staticmethod
    async def delete_user(
        uow: AbstractUnitOfWork,
        filters: Optional[UserFilter] = None
    ) -> UserIDBSchema:
        async with uow:
            result: UserModel = await uow.user.delete_one(filters=filters)
            return UserIDBSchema(**result.__dict__)