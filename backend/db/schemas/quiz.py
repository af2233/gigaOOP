from pydantic import BaseModel
from typing import List, Optional


class QuizQuestionAnswerBase(BaseModel):
    answer_text: str
    is_correct: bool


class QuizQuestionAnswerCreate(QuizQuestionAnswerBase):
    pass


class QuizQuestionAnswerRead(QuizQuestionAnswerBase):
    id: int

    class ConfigDict:
        from_attributes = True


class QuizQuestionBase(BaseModel):
    question_text: str


class QuizQuestionCreate(QuizQuestionBase):
    answers: List[QuizQuestionAnswerCreate]


class QuizQuestionRead(QuizQuestionBase):
    id: int
    answers: List[QuizQuestionAnswerRead]

    class ConfigDict:
        from_attributes = True


class QuizBase(BaseModel):
    title: str
    description: str
    theme_id: int


class QuizCreate(QuizBase):
    questions: List[QuizQuestionCreate] = []


class QuizRead(QuizBase):
    id: int
    questions: List[QuizQuestionRead] = []

    class ConfigDict:
        from_attributes = True


class QuizUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    questions: Optional[List[QuizQuestionCreate]] = None
    theme_id: Optional[int] = None
