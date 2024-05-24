from pydantic import BaseModel


class ThemeBase(BaseModel):
    title: str
    description: str


class ThemeCreate(ThemeBase):
    course_id: int


class ThemeUpdate(ThemeBase):
    pass


class ThemeInDB(ThemeBase):
    id: int
