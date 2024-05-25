from pydantic import BaseModel


class QuestionBase(BaseModel):
    quiz_id: int
    question_text: str


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(QuestionBase):
    quiz_id: int | None = None
    question_text: str | None = None


class QuestionRead(QuestionBase):
    id: int

    class Config:
        orm_mode = True
