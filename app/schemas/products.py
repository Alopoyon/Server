from pydantic import BaseModel
from typing import Optional

class Category(BaseModel):
    id: str
    name: str

    class Config:
        from_attributes=True

class BaseProduct(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    description: Optional[str] = None

    class Config:
        from_attributes=True


class Product(BaseProduct):
    category: Optional[Category]