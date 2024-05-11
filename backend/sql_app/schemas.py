from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    login: str
    password: str
    email: EmailStr


class User(UserBase):
    id: int
    status: int
    fullname: str

    class Config:
        orm_mode = True
