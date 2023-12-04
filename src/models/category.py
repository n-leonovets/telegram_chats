from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base, str64


class CategoryModel(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str64]
    parent_id: Mapped[int] = mapped_column(server_default="0")
