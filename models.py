from sqlalchemy import Column, String, DateTime, Integer, ARRAY
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel, EmailStr

Base = declarative_base()

class SystemInfo(Base):
    __tablename__ = "system_info"
    id = Column(Integer, primary_key=True)
    version = Column(ARRAY(Integer))
    user_email = Column(String)
    request_date = Column(DateTime)

class VersionRequest(BaseModel):
    user_email: EmailStr