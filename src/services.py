from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from models import SystemInfo
from datetime import datetime

def get_next_version(current_version: str):
    parts = list(map(int, current_version.split(".")))
    parts[-1] += 1
    for i in reversed(range(1, len(parts))):
        if parts[i] >= 11: 
            parts[i] = 0
            parts[i-1] += 1
    return ".".join(map(str, parts))

def get_current_version(db: Session):
    try:
        latest_version = db.query(SystemInfo).order_by(SystemInfo.version.desc()).first()
        if latest_version:
            return {"version": ".".join(map(str, latest_version.version))} 
        else:
            return {"version": "0.0.0"}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro no banco de dados: {e}")

def save_new_version(version_request, db: Session):
    try:
        latest_version = db.query(SystemInfo).order_by(SystemInfo.version.desc()).first()
        current_version = latest_version.version if latest_version else [0, 0, 0] 
        current_version_str = ".".join(map(str, current_version)) 
        new_version_str = get_next_version(current_version_str)
        new_version = list(map(int, new_version_str.split("."))) 

        new_version_entry = SystemInfo(
            version=new_version, 
            user_email=version_request.user_email,
            request_date=datetime.now(),
        )
        db.add(new_version_entry)
        db.commit()
        return {"version": new_version_str}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Erro na versão: {e}")
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erro no banco de dados: {e}")