import os
import logging

from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str = "Telegram Chats"
    DEBUG: bool = os.environ.get('DEBUG', False)

    AUTH_SECRET_KEY: str = os.environ.get("AUTH_SECRET_KEY", "...")
    AUTH_ALGORITHM: str = os.environ.get("AUTH_ALGORITHM", "...")

    ADMIN_USERNAME: str = os.environ.get("ADMIN_USERNAME", "username")
    ADMIN_HASHED_PASSWORD: str = os.environ.get("ADMIN_HASHED_PASSWORD", "password")

    DB_USER: str = os.environ.get("DB_USER", "postgres")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD", "postgres")
    DB_HOST: str = os.environ.get("DB_HOST", "localhost")
    DB_PORT: int = os.environ.get("DB_PORT", "5432")
    DB_DATABASE: str = os.environ.get("DB_DATABASE", "jobhub")

    @property
    def get_asyncpg_url(self):
        return (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
                f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DATABASE}")

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()


logging.basicConfig(
    level=logging.INFO,
    filename="src/logs/main.log",
    encoding="utf-8",
    format="%(asctime)s [%(levelname)s] %(message)s"
)
