from sqlalchemy import Boolean, Column, Integer, String, Float, Text
from sqlalchemy.orm import relationship

from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255), index=True, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float(2), default=0.0)
    quantity = Column(Integer, default=0)
    category = Column(String, nullable=True)
    # image = Column(String, default="No Image") # URL to aome other database or something, look into it later
    metadata = Column(Text, nullable=True) # TBD an array/comma separated strings that help match the product
    published = Column(Boolean, default=False)
    


