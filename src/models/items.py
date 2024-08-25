from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserIn(BaseModel):
    username: Optional[str]
    passowrd: str
    email: EmailStr
    full_name: Optional[str] | None = None
    signin_ts: datetime | None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserInDB(BaseModel):
    username: str
    passowrd: str
    email: EmailStr
    full_name: str | None = None