from sqlalchemy.orm import Session

from app.models.users import User
from app.schemas.users import UserCreate, UserEmail

import uuid

def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.uid == user_id).first()


def get_user_by_email(db: Session, email: UserEmail):
    # print(f"\n\n\n{email.email}\n\n\n")
    return db.query(User).filter(User.email == email.email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(uid=str(uuid.uuid4()),
                   username=user.username, 
                   email=user.email,
                   password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
