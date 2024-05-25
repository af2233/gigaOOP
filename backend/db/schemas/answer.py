from pydantic import BaseModel


class AnswerBase(BaseModel):
    question_id: int
    answer_text: str
    proper: int


class AnswerCreate(AnswerBase):
    pass


class AnswerUpdate(AnswerBase):
    quiz_id: int | None = None
    question_text: str | None = None


class AnswerRead(AnswerBase):
    id: int

    class Config:
        orm_mode = True
