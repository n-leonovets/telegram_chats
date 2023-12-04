from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base, created_at, updated_at


class ChatCategoryModel(Base):
    __tablename__ = "chat_category"

    chat_id: Mapped[int] = mapped_column(ForeignKey("chat.id", ondelete="CASCADE"), primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id", ondelete="CASCADE"), primary_key=True)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
