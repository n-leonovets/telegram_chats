from typing import Optional

from src.models.user import UserModel
from src.schemas.user import UserIDBSchema
from src.services.filters.base import LimitFilter
from src.services.filters.user import UserFilter
from src.utils.unitofwork import AbstractUnitOfWork


class UserService:
    @staticmethod
    async def get_user(
        uow: AbstractUnitOfWork,
        filters: Optional[UserFilter] = None,
        limits: Optional[LimitFilter] = None
    ) -> UserIDBSchema:
        async with uow:
            result: UserModel = await uow.user.read_one(filters=filters, limits=limits)
            return UserIDBSchema(**result.__dict__)
