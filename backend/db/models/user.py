from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from ...db.session import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    name: Mapped[str] = mapped_column(String(length=320), nullable=True)
    status: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
