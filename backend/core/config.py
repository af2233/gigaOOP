class Settings:
    PROJECT_NAME: str = 'gigaOOP'
    PROJECT_VERSION: str = '0.0.1'

    SQLITE_DB = '/backend/gigaOOP_database.db'
    DATABASE_URL = f'sqlite://{SQLITE_DB}'


settings = Settings()
