from typing import Annotated

from fastapi import Depends

# from src.api.auth import required_auth
# from src.schemas.user import UserPublic
from src.utils.unitofwork import AbstractUnitOfWork, UnitOfWork


UOWDep = Annotated[AbstractUnitOfWork, Depends(UnitOfWork)]
# AuthDep = Annotated[UserPublic, Depends(required_auth)]
