from pydantic import BaseModel


class ThemeBase(BaseModel):
    title: str
    description: str


class ThemeCreate(ThemeBase):
    pass


class ThemeUpdate(ThemeBase):
    pass


class ThemeInDB(ThemeBase):
    id: int
    course_id: int
