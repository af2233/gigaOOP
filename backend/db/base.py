from ..db.session import engine, Base
from ..db.models.user import User
from ..db.models.course import Course
from ..db.models.theme import Theme
from ..db.models.quiz import Quiz
from ..db.models.question import Question
from ..db.models.answer import Answer
from ..db.models.user_answer import UserAnswer


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
