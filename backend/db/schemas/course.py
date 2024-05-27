from pydantic import BaseModel


class CourseBase(BaseModel):
    title: str
    description: str


class CourseCreate(CourseBase):
    pass


class CourseUpdate(CourseBase):
    title: str | None = None
    description: str | None = None


class CourseRead(CourseBase):
    id: int

    class ConfigDict:
        from_attributes = True
