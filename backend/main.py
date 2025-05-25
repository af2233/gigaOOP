import uuid
import logging
import uvicorn

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import course, quiz, theme, user
from core.auth import auth_backend
from core.config import settings
from db.schemas.user import UserCreate, UserRead, UserUpdate


# Logging setup
logging.basicConfig(level=logging.INFO)

# Main app setup
app = FastAPI(title=settings.PROJECT_NAME,
              summary=settings.SUMMARY,
              descriptions=settings.DESCRIPTION,
              version=settings.PROJECT_VERSION,
              license_info=settings.LICENSE_INFO,
              openapi_tags=settings.TAGS_METADATA,
              docs_url=None,
              redoc_url=None,
              )

# login/logout routers
app.include_router(
    user.fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

# register router
app.include_router(
    user.fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    user.fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
    deprecated=True,
)

app.include_router(
    user.fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
    deprecated=True,
)

app.include_router(
    user.fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
    deprecated=True,
)

app.include_router(
    course.router,
    prefix="/courses",
    tags=["courses"],
)

app.include_router(
    theme.router,
    prefix="/themes",
    tags=["themes"],
)

app.include_router(
    quiz.router,
    prefix="/quizzes",
    tags=["quizzes"],
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://0.0.0.0:5173",
    "http://frontend:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
