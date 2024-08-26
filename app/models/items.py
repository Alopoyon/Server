from pydantic import BaseModel
from typing import Optional
class Product(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None

    class Config:
        orm_mode=True

class Category(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode=True

class ProductCategory(BaseModel):
    product_id: int
    category_id: int