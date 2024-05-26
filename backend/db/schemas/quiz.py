from pydantic import BaseModel
from typing import List, Optional

class QuizQuestionBase(BaseModel):
    question_text: str
    answer: str

class QuizQuestionCreate(QuizQuestionBase):
    pass

class QuizQuestionRead(QuizQuestionBase):
    id: int

    class Config:
        orm_mode = True

class QuizBase(BaseModel):
    title: str
    description: str
    course_id: int
    theme_id: int

class QuizCreate(QuizBase):
    questions: List[QuizQuestionCreate] = []

class QuizRead(QuizBase):
    id: int
    questions: List[QuizQuestionRead] = []

    class Config:
        orm_mode = True

class QuizUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    questions: Optional[List[QuizQuestionCreate]] = None
    theme_id: Optional[int] = None
