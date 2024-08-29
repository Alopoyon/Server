from pydantic import BaseModel, validator, EmailStr, SecretStr
from typing import Optional
from datetime import datetime


class BaseUser(BaseModel):
    uid: str
    username: Optional[str]
    email: EmailStr
    full_name: Optional[str] | None = None

class Password(BaseModel):
    # PASSWORD_REGEX = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]+$"

    password: str

    # @validator("password", always=False)
    # def validate_password(cls, value, values):
    #     if values.get("is_new_user"):
    #         # - Check for common weak passwords
    #         # - Ensure password is not part of a leaked database
    #         ...
    #     return value

class UserIn(BaseUser):
    password: Password
    signin_ts: datetime | None

    class Config:
        from_attributes=True

class UserOut(BaseUser):
    signout_ts: datetime | None
    
    class Config:
        from_attributes=True

class Address(BaseModel):
    street: str
    city: str
    state: str

class UserCreate(Password, BaseUser):
    address: Optional[Address] | None = None
    signin_count: int
    is_active: bool = False

    class Config:
        from_attributes=True

class UserEmail(BaseModel):
    email: EmailStr

    class Config:
        from_attributes=True

