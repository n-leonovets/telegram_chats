from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base, str64


class UserModel(Base):
    __tablename__ = "user"

    username: Mapped[str64] = mapped_column(primary_key=True, autoincrement=False)
    fullname: Mapped[str64]
    hashed_password: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(server_default="false")
    is_disabled: Mapped[bool] = mapped_column(server_default="false")
