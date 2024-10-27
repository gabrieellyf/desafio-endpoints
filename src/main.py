from fastapi import FastAPI, Depends, status
from models import VersionRequest
from database import engine, get_db, Session
from services import get_current_version, save_new_version
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/version")
def get_current_version_endpoint(db: Session = Depends(get_db)):
    return get_current_version(db)

@app.post("/version", status_code=status.HTTP_201_CREATED)
def save_new_version_endpoint(version_request: VersionRequest, db: Session = Depends(get_db)):
    return save_new_version(version_request, db)