from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    name: str
    password: str = Field(..., min_length=4)
    login: str


class User(UserBase):
    id: int
    status: int

    class Config:
        orm_mode = True
