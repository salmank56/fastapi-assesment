from sqlalchemy import Column, Integer, String, text, DateTime, func
from app.db import Base

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, server_default=text("nextval('clients_id_seq')"))
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())