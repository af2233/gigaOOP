from backend.db.session import engine, Base
from backend.db.models.user import User
from backend.db.models.course import Course


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
