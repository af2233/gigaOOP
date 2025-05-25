import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "gigaOOP"
    SUMMARY: str = "IT project - OOP Educational Platform"
    DESCRIPTION: str = "A web service with basic mechanisms for a working educational platform for studying OOP"
    PROJECT_VERSION: str = "1.0.0"
    LICENSE_INFO: dict = {"name": "Apache 2.0", "identifier": "MIT"}
    TAGS_METADATA: list = [
        {"name": "auth", "description": "The login **logic** is here."},
        {"name": "users", "description": "Operations with users."},
        {"name": "courses", "description": ""},
        {"name": "themes", "description": ""},
        {"name": "quizzes", "description": ""}
    ]

    DB_NAME = os.environ.get("DB_NAME")
    DB_URL = f"sqlite+aiosqlite:///./{DB_NAME}.db"

    SECRET_AUTH = os.environ.get("SECRET_AUTH")


settings = Settings()
