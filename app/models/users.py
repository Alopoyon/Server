from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    uid = Column(String(32), primary_key=True)
    username = Column(String(255), nullable=True, default="")
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=False)
    signin_count = Column(Integer, default=0)


