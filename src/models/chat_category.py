from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src_base.database import Base, str64


class ChatCategoryTable(Base):
    __tablename__ = "chat_category"

    chat_id: Mapped[int] = mapped_column(ForeignKey("chat.id", ondelete="CASCADE"), primary_key=True)
    category: Mapped[str64]
