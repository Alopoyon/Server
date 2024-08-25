from pydantic import BaseModel, EmailStr

class UserIn(BaseModel):
    username: str
    passowrd: str
    email: EmailStr
    full_name: str | None = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserInDB(BaseModel):
    username: str
    passowrd: str
    email: EmailStr
    full_name: str | None = None