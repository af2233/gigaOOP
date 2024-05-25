from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users.db import SQLAlchemyUserDatabase

from db.session import Base, get_async_session


class User(SQLAlchemyBaseUserTableUUID, Base):
    name: Mapped[str] = mapped_column(String(length=320), nullable=True)
    status: Mapped[int] = mapped_column(Integer, default=0, nullable=False)


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
