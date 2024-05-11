from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/users/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')

    db_user = crud.get_user_by_login(db, login=user.login)

    if db_user:
        raise HTTPException(status_code=400, detail='Login already registered')

    return crud.create_user(db=db, user=user)


@app.get('/users/{user_id}', response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return db_user


@app.delete('/users/{user_id}', response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return crud.delete_user(db=db, user_id=user_id)


@app.put('/users/{user_id}', response_model=schemas.User)
def update_email(user_id: int, email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    db_user = crud.get_user_by_email(db, email=email)

    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')

    return crud.update_email(db=db, user_id=user_id, email=email)


@app.put('/users/{user_id}', response_model=schemas.User)
def update_password(user_id: int, password: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return crud.update_password(db=db, user_id=user_id, password=password)


@app.put('/users/{user_id}', response_model=schemas.User)
def update_login(user_id: int, login: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    db_user = crud.get_user_by_login(db, login=login)

    if db_user:
        raise HTTPException(status_code=400, detail='Login already registered')

    return crud.update_login(db=db, user_id=user_id, login=login)
