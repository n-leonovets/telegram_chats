import logging

from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    APP_NAME: str = "Telegram Chats"
    DEBUG: bool = False

    AUTH_SECRET_KEY: str
    AUTH_ALGORITHM: str

    ADMIN_USERNAME: str
    ADMIN_HASHED_PASSWORD: str

    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_DATABASE: str

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
