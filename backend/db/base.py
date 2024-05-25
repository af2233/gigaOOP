from db.session import engine, Base
from db.models.user import User
from db.models.course import Course
from db.models.theme import Theme


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
