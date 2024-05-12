from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.models import Base
from backend.core.config import settings
from backend.app.routes import router
from backend.app.session import engine


Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(router)

origins = [
    'http://localhost',
    'http://localhost:5173',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
def read_root():
    return {'Hello': 'World'}
