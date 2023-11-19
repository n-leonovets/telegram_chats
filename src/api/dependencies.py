from src.repositories.chat import ChatRepository
from src.services.chat import ChatService


def chat_service():
    return ChatService(ChatRepository())
