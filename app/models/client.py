from sqlalchemy import Column, Integer, String
from app.db import Base

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True, server_default="nextval('clients_id_seq'::regclass)")
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
