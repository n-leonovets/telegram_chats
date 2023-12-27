from typing import Annotated

from fastapi import Depends

from src.api.auth import required_auth
from src.schemas.user import UserPublic

AuthDep = Annotated[UserPublic, Depends(required_auth)]
