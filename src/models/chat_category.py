from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base, bigint


class ChatCategoryModel(Base):
    __tablename__ = "chat_category"

    chat_id: Mapped[bigint] = mapped_column(ForeignKey("chat.id", ondelete="CASCADE"), primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id", ondelete="CASCADE"), primary_key=True)
