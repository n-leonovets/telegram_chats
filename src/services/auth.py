from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    @staticmethod
    def create_access_token(username: str, duration_minutes: int | None = 60) -> str:
        access_token = jwt.encode(
            claims={
                "username": username,
                "type": "access",
                "exp": datetime.utcnow() + timedelta(minutes=duration_minutes)
            },
            key=settings.AUTH_SECRET_KEY,
            algorithm=settings.AUTH_ALGORITHM
        )
        return access_token

    @staticmethod
    def create_refresh_token(username: str, duration_days: int = 7) -> str:
        refresh_token = jwt.encode(
            claims={
                "username": username,
                "type": "refresh",
                "exp": datetime.utcnow() + timedelta(days=duration_days)
            },
            key=settings.AUTH_SECRET_KEY,
            algorithm=settings.AUTH_ALGORITHM
        )
        return refresh_token

    @staticmethod
    def get_password_hash(password) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password, hashed_password) -> bool:
        return pwd_context.verify(plain_password, hashed_password)
