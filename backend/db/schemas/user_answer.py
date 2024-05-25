from pydantic import BaseModel

# U - User, A - Answer


class UABase(BaseModel):
    user_id: int
    question_id: int
    quiz_id: int


class UACreate(UABase):
    pass


class UAUpdate(UABase):
    user_id: int | None = None
    question_id: int | None = None
    quiz_id: int | None = None


class UARead(UABase):
    id: int

    class Config:
        orm_mode = True
