import asyncio
import json
from pathlib import Path

from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import async_session_maker, engine, Base
from db.models.course import Course
from db.models.theme import Theme
from db.models.quiz import Quiz, QuizQuestion, QuizQuestionAnswer


DATA_DIR = Path(__file__).parent / "data"


async def check_tables_exist():
    async with engine.begin() as conn:
        def do_inspect(sync_conn):
            inspector = inspect(sync_conn)
            tables = inspector.get_table_names()
            if "courses" not in tables:
                raise Exception("No tables created. Please run alembic upgrade head.")

        await conn.run_sync(do_inspect)


async def load_json(filename: str) -> list[dict]:
    with open(DATA_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)


async def insert_entities(session: AsyncSession, model, data: list[dict]):
    for item in data:
        session.add(model(**item))


async def load_data():
    await check_tables_exist()

    async with async_session_maker() as session:
        await insert_entities(session, Course, await load_json("courses.json"))
        await insert_entities(session, Theme, await load_json("themes.json"))
        await insert_entities(session, Quiz, await load_json("quizzes.json"))
        await insert_entities(session, QuizQuestion, await load_json("questions.json"))
        await insert_entities(session, QuizQuestionAnswer, await load_json("answers.json"))

        await session.commit()


if __name__ == "__main__":
    asyncio.run(load_data())
    print('Data dumped into database.')
