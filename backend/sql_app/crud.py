from sqlalchemy.orm import Session

import models
import schemas

from backend import hashing


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):

    hashed_password = hashing.hash_password(user.password)  # хеширование пароля
    hashed_email = hashing.hash_email(user.email)  # хеширование почты

    db_user = models.User(name=user.name, email=hashed_email, hashed_password=hashed_password, nickname=user.login)
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

    hashed_email = hashing.hash_email(email)  # хеширование почты

    db_user.email = hashed_email
    db.commit()
    db.refresh(db_user)
    return db_user


def update_password(db: Session, user_id: int, password: str):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    hashed_password = hashing.hash_password(password)  # хеширование пароля

    db_user.password = hashed_password
    db.commit()
    db.refresh(db_user)
    return db_user
