from fastapi.applications import Depends
from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.users import UserCreate, UserEmail, BaseUser
from app.crud import users as userCRUD

router = APIRouter()

@router.get("/")#, include_in_schema=False)
async def read_prducts():
    return [{"users": "none"}]

@router.post("/get_user_by_email/", response_model= BaseUser)
async def get_user(user_email: UserEmail, db: Session = Depends(get_db)):
    # _r =  userCRUD.get_user_by_email(db=db, email=user.email)
    # print("get User by email: ",_r)
    return userCRUD.get_user_by_email(db=db, email=user_email)


@router.post("/create_new_user/", response_model=UserCreate)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    # db_user = userCRUD.get_user_by_email(db= db, email = user.email)
    # print("Result of create new user: ",db_user)
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email already registered!")
    return userCRUD.create_user(db= db, user= user)

#   "username": "jhon",
#   "email": "jhon@domain.com",
#   "full_name": "Jhon Doe",
#   "password": "P@ssword",
#   "address": {
#     "street": "12 Kennedy St",
#      "city": "Ougadougau",
#      "state": "AL"
#   },
#   "signin_count": 0,
#   "is_active": false