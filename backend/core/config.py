import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "gigaOOP"
    PROJECT_VERSION: str = "1.0.0"

    DB_NAME = os.environ.get("DB_NAME")
    DB_URL = f"sqlite+aiosqlite:///./{DB_NAME}.db"
    TEST_DB_NAME = os.environ.get("DB_NAME_TEST")
    TEST_DB_URL = f"sqlite+aiosqlite:///./{TEST_DB_NAME}.db"
    SECRET_AUTH = os.environ.get("SECRET_AUTH")


settings = Settings()
