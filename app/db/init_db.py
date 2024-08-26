from app.db.base import Base
from app.db.session import SessionLocal, engine

Base.metadata.create_all(bind=engine)

def init_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()