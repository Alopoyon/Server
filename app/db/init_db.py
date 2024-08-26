import app.models as models
from app.db.session import SessionLocal, engine


def init_db():
     models.metadata.create_all(bind=engine)