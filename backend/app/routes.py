from fastapi import Depends, HTTPException, APIRouter

from .crud import *
from .schemas import User, UserCreate
from .session import get_db


router = APIRouter(prefix='/users', tags=['User'])


@router.post('/', response_model=User)
def post_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')

    db_user = get_user_by_login(db, login=user.login)

    if db_user:
        raise HTTPException(status_code=400, detail='Login already registered')

    return create_user(db=db, user=user)


@router.get('/{user_id}', response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return db_user


@router.delete('/{user_id}', response_model=User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return delete_user(db=db, user_id=user_id)


@router.put('/{user_id}', response_model=User)
def update_password(user_id: int, password: str, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return update_password(db=db, user_id=user_id, password=password)


'''
@router.put('/{user_id}', response_model=User)
def update_email(user_id: int, email: str, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    db_user = get_user_by_email(db, email=email)

    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')

    return update_email(db=db, user_id=user_id, email=email)


@router.put('/{user_id}', response_model=User)
def update_login(user_id: int, login: str, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')

    db_user = get_user_by_login(db, login=login)

    if db_user:
        raise HTTPException(status_code=400, detail='Login already registered')

    return update_login(db=db, user_id=user_id, login=login)
'''
