from sqlalchemy import Column, Integer, String, text, DateTime, func
from app.db import Base
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class Client(Base):
    __tablename__ = "clients"
    id = Column(String(16), primary_key=True, index=True, default=lambda: str(uuid4())) 
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())