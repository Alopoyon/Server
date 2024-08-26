from pydantic import BaseModel
from typing import Optional

class Category(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode=True

class BaseProduct(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None

    class Config:
        orm_mode=True


class Product(BaseProduct,Category):
    ...