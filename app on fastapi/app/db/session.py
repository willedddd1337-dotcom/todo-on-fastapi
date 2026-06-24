from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import get_settings

settings = get_settings()

engine = create_engine(settings.data_base_url)


Sesionlocal = sessionmaker[Session](bind=engine)


def get_db(): 
    db = Sesionlocal()
    
    try: 
        yield db 
    finally: 
        db.close()