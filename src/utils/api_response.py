from typing import Optional, Generic, TypeVar

from pydantic import BaseModel


T = TypeVar("T")


class ApiError(BaseModel):
    """
    Стардартизированный ответ ошибок API.

        Parameters:
            module (``str``):
                Имя модуля, где возникла ошибка.

            name (``str``):
                Имя ошибки.

            message (``str``):
                Сообщение ошибки.
    """
    module: str
    name: str
    message: str


class ApiResponse(BaseModel, Generic[T]):
    """
    Стардартизированный ответ API.

        Parameters:
            status_code (``int``):
                Статус ответ сервера.

            data (Any | None) = None:
                Выходные данные.

            details (ApiError | None) = None:
                Детали ошибок.
    """
    status_code: int
    data: Optional[T] = None
    details: Optional[ApiError] = None
