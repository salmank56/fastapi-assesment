from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID


class ClientCreate(BaseModel):
    name: str
    email: EmailStr

class ClientResponse(BaseModel):
    id: UUID
    name: str
    email: str
    created_at: datetime
    
class ClientUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None

    class Config:
        orm_mode = True
