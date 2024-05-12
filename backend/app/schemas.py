from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    name: str | None = None
    email: str
    password: str = Field(..., min_length=4)
    login: str
    


class UserCreate(UserBase):
    email: EmailStr
    password: str = Field(..., min_length=4)
    login: str


class User(UserBase):
    id: int
    status: int

    class Config:
        orm_mode = True
