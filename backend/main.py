from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from . import crud, models, schemas

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {'Hello': 'World'}

@app.post("/users")
def create_user(user: User):
    pass
