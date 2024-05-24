from pydantic import BaseModel


class CourseBase(BaseModel):
    title: str
    description: str


class CourseCreate(CourseBase):
    pass


class CourseUpdate(CourseBase):
    pass


class CourseInDB(CourseBase):
    id: int
    instructor_id: int
