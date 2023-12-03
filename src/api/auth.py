import logging

from typing import Annotated

from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

from src.api.dependencies import UOWDep
from src.schemas.auth import AuthTokens, Token
from src.schemas.user import UserIDBSchema
from src.services.auth import AuthService
from src.services.filters.user import UserFilter
from src.services.user import UserService
from config import settings
from src.utils.api_response import ApiResponse

_logger = logging.getLogger(__name__)
router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def required_auth(
    uow: UOWDep,
    access_token: Annotated[str, Depends(oauth2_scheme)]
) -> UserIDBSchema:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token=access_token,
            key=settings.AUTH_SECRET_KEY,
            algorithms=[settings.AUTH_ALGORITHM]
        )
        username: str = payload.get("username")
        token_type: str = payload.get("type")
        if username is None or not token_type == "access":
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await UserService().get_user(uow=uow, filters=UserFilter(username=username))
    if user is None or user.is_disabled:
        raise credentials_exception

    return user


@router.post("/login")
async def login_for_access_token(
    uow: UOWDep,
    form: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> ApiResponse[AuthTokens]:
    user = await UserService().get_user(uow, filters=UserFilter(username=form.username))
    verify_password = AuthService().verify_password(form.password, user.hashed_password)

    if not user or not verify_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = AuthService().create_access_token(username=form.username)
    refresh_token = AuthService().create_refresh_token(username=form.username)
    
    return ApiResponse(
        status_code=status.HTTP_200_OK,
        data=AuthTokens(
            access_token=Token(
                token=access_token,
                token_type="bearer"
            ),
            refresh_token=Token(
                token=refresh_token,
                token_type="bearer"
            )
        )
    )


@router.post("/refresh_token")
async def get_new_token(
    uow: UOWDep,
    refresh_token: str = Depends(oauth2_scheme)
) -> ApiResponse[AuthTokens]:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token=refresh_token,
            key=settings.AUTH_SECRET_KEY,
            algorithms=[settings.AUTH_ALGORITHM]
        )
        username: str = payload.get("username")
        token_type: str = payload.get("type")
        if username is None or token_type != "refresh":
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await UserService().get_user(uow=uow, filters=UserFilter(username=username))
    if user is None or user.is_disabled:
        raise credentials_exception

    access_token = AuthService().create_access_token(username=username)
    refresh_token = AuthService().create_refresh_token(username=username)

    return ApiResponse(
        status_code=status.HTTP_200_OK,
        data=AuthTokens(
            access_token=Token(
                token=access_token,
                token_type="bearer"
            ),
            refresh_token=Token(
                token=refresh_token,
                token_type="bearer"
            )
        )
    )
