from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker, Session

host = 'localhost'
dbname = 'system_info'
user = 'postgres'
password = '1234'  
port = 5432  
DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

__all__ = ["engine", "get_db", "SessionLocal", "Session"] 

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()