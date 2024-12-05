from pydantic import BaseModel, EmailStr
from datetime import datetime

class ClientCreate(BaseModel):
    name: str
    email: EmailStr

class ClientResponse(ClientCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
