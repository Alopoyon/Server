from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

class BaseUser(BaseModel):
    username: Optional[str]
    email: EmailStr
    full_name: Optional[str] | None = None

class Password(BaseModel):
    PASSWORD_REGEX = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]+$"

    password: str = Field(min_length=8, max_length=128, regex=PASSWORD_REGEX)

    @validator("password", always=False)
    def validate_password(cls, value, values):
        if values.get("is_new_user"):
            # - Check for common weak passwords
            # - Ensure password is not part of a leaked database
            ...
        return value

class UserIn(BaseUser):
    password: Password
    signin_ts: datetime | None

    class Config:
        orm_mode=True

class UserOut(BaseUser):
    signout_ts: datetime | None
    
    class Config:
        orm_mode=True

class Address(BaseModel):
    street: str
    city: str
    state: str

class UserCreate(BaseUser,Password):
    address: Optional[Address] | None = None
    signin_count: int

    class Config:
        orm_mode=True

