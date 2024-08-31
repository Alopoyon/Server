from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.users import User
from app.schemas.users import UserCreate, UserEmail

import uuid

def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.uid == user_id).first()


def get_user_by_email(db: Session, email: UserEmail):
    # print(f"\n\n\n{email.email}\n\n\n")
    return db.query(User).filter(User.email == email.email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    _res = db.execute(
        select(User.uid, User.email, User.username, User.is_active, User.signin_count)
        .offset(skip)
        .limit(limit)
    ).all()
    _res  = convert_retrived_user_data_to_json(_res)
    # _resp = []
    # for user in _res:
    #     _user_dict = user.__dict__
    #     del _user_dict['_sa_instance_state']
    #     _resp.append(_user_dict)
    # print(f"{_resp=}")
    return _res


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

def convert_retrived_user_data_to_json(userList: list):
    _new_resp = []
    for user in userList:
        _tempUser = {}
        _tempUser['uid']=user[0]
        _tempUser['email']=user[1]
        _tempUser['username']=user[2]
        _tempUser['is_active']=user[3]
        _tempUser['signin_count']=user[4]
        _new_resp.append(_tempUser)
    return _new_resp