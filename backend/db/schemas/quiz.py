from pydantic import BaseModel


class QuizBase(BaseModel):
    theme_id: int


class QuizCreate(QuizBase):
    pass


class QuizUpdate(QuizBase):
    theme_id: int | None = None


class QuizRead(QuizBase):
    id: int

    class Config:
        orm_mode = True
