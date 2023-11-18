from src_base.repositories.chat import ChatRepository
from src_base.services.chat import ChatService


def chat_service():
    return ChatService(ChatRepository())
