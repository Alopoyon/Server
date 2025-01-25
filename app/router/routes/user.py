from fastapi.applications import Depends
from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.users import UserCreate, UserEmail, BaseUser, UserList
from app.crud import users as userCRUD

router = APIRouter()

@router.get("/", include_in_schema=False)
async def read_prducts():
    return [{"users": "none"}]

@router.get("/get_users/", response_model= UserList)
async def get_users(skip: int =0, limit: int =10, db: Session = Depends(get_db)):
    try:
        _userList = userCRUD.get_users(db=db, skip=skip, limit=limit)
    except:
        raise HTTPException(
            status_code=404,
            detail="Failed to retrieve users",
            headers={"X-Error": "There goes my error"}
        )
    return _userList


@router.post("/get_user_by_email/", response_model= BaseUser)
async def get_user_by_email(user_email: UserEmail, db: Session = Depends(get_db)):
    try:
        _user = userCRUD.get_user_by_email(db=db, email=user_email)
        if user_email not in _user.values():
            raise HTTPException(            
                status_code=404,
                detail="User not found",
                headers={"X-Error": "User not in database"})
    except:
        raise HTTPException(
            status_code=404,
            detail="Failed to retrieve user",
            headers={"X-Error": "There goes my error"}
        )

    return _user


@router.post("/create_new_user/", response_model=UserCreate)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    _userCheck = userCRUD.get_user_by_email(db= db, email = user.email)
    if _userCheck:
        raise HTTPException(status_code=400, detail="Email already registered!")
    return userCRUD.create_user(db= db, user= user)
