from aiohttp import ClintSession


class Client:
    """Клиент для работы с API.
    Его вызывают все другие микросервисы, которые взаимодействуют с telegram_chats, как с библиотекой.

    Пример:
        from telegram_chats import Client as TelegramChats

        chats = await TelegramChats.get_chats(filters)
    """
    def __init__(
        self,
        access_token: str,
        refresh_token: str,
        address: str = "localhost"
    ):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.address = address

    def _get(self):
        pass

    def _post(self):
        pass

    def _path(self):
        pass

    def _delete(self):
        pass
