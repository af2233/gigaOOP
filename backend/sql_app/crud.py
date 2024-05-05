from sqlalchemy.orm import Session

import models
import schemas

from backend import fun_for_hash_data


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):

    hashed_password = (fun_for_hash_data.User(user.nickname, user.password, user.email)).hash_password()

    db_user = models.User(name=user.name, email=user.email, hashed_password=hashed_password, nickname=user.nickname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return db_user


def update_email(db: Session, user_id: int, email: str):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db_user.email = email
    db.commit()
    db.refresh(db_user)
    return db_user
