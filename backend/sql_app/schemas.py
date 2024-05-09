from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    name: str
    password: str
    login: str


class User(UserBase):
    id: int
    status: int

    class Config:
        orm_mode = True
