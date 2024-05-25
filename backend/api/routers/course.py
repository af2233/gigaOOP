from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import async_session_maker
from db.models.course import Course
from db.schemas.course import CourseCreate, CourseUpdate, CourseInDB

course_router = APIRouter()


async def get_db() -> AsyncSession:
    async with async_session_maker() as session:
        yield session


@course_router.post("/", response_model=CourseInDB)
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    db_course = Course(**course.dict())
    db.add(db_course)
    await db.commit()
    await db.refresh(db_course)
    return db_course


@course_router.get("/{course_id}", response_model=CourseInDB)
async def read_course(course_id: int, db: AsyncSession = Depends(get_db)):
    course = await db.get(Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
