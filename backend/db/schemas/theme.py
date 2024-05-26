from pydantic import BaseModel


class ThemeBase(BaseModel):
    title: str
    content: str
    course_id: int


class ThemeCreate(ThemeBase):
    pass


class ThemeUpdate(ThemeBase):
    title: str | None = None
    content: str | None = None
    course_id: int | None = None


class ThemeRead(ThemeBase):
    id: int

    class Config:
        orm_mode = True
