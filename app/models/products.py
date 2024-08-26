from sqlalchemy import Boolean, Column, Integer, String, Float, Text
from sqlalchemy.orm import relationship

from app.db.init_db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), index=True)
    description = Column(Text)
    price = Column(Float(2), default=0.0)
    quantity = Column(Integer, default=0)
    # image = Column(String, default="No Image") # URL to aome other database or something, look into it later
    metadata = Column(Text) # TBD an array/comma separated strings that help match the product
    published = Column(Boolean, default=False)
    


