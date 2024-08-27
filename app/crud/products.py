from sqlalchemy.orm import Session

from app.models.products import Product
from app.schemas.products import Product as ProductCreate

def get_product(db: Session, name: str):
    return db.query(Product).filter(Product.name == name).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    db.query(Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: ProductCreate):
    db_product = Product(name=product.name, price=product.price, description=product.description)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
