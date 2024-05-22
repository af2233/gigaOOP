from typing import Optional
import uuid
from fastapi_users import schemas

class UserRead(schemas.BaseUser[uuid.UUID]):
    name: Optional[str] = None
    status: int = 0

class UserCreate(schemas.BaseUserCreate):
    name: Optional[str] = None
    status: int = 0

class UserUpdate(schemas.BaseUserUpdate):
    name: Optional[str] = None
    status: int = None