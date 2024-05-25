from contextlib import asynccontextmanager
import uuid

from fastapi import Depends, FastAPI
from fastapi_users import FastAPIUsers

from fastapi.middleware.cors import CORSMiddleware
import logging

from backend.api.routers.course import course_router
from backend.api.routers.theme import theme_router
from backend.api.routers.user import current_active_user, fastapi_users, get_user_manager
from backend.core.auth import auth_backend
from backend.core.config import settings
from backend.db.schemas.user import UserCreate, UserRead, UserUpdate
from backend.db.models.user import User
from backend.db.base import create_db_and_tables


# Настройка логирования
logging.basicConfig(level=logging.DEBUG)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION, lifespan=lifespan)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

# app.include_router(
#     fastapi_users.get_reset_password_router(),
#     prefix="/auth",
#     tags=["auth"],
# )
# app.include_router(
#     fastapi_users.get_verify_router(UserRead),
#     prefix="/auth",
#     tags=["auth"],
# )
# app.include_router(
#     fastapi_users.get_users_router(UserRead, UserUpdate),
#     prefix="/users",
#     tags=["users"],
# )

app.include_router(course_router, prefix="/courses", tags=["courses"])

app.include_router(theme_router, prefix="/themes", tags=["themes"])


origins = [
    'http://localhost',
    'http://localhost:5173',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET, POST, PATCH, DELETE'],
    allow_headers=['*'],
)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}
