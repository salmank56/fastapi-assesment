from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.client import (
    get_all_clients,
    get_client_by_id,
    create_client,
    update_client,
    delete_client,
)
from app.schemas.client import ClientCreate, ClientResponse
from app.db import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/clients", response_model=ClientResponse, status_code=201)
def create_new_client(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db, client)

@router.get("/clients", response_model=list[ClientResponse])
def read_clients(db: Session = Depends(get_db)):
    return get_all_clients(db)

@router.get("/clients/{client_id}", response_model=ClientResponse)
def read_client(client_id: int, db: Session = Depends(get_db)):
    client = get_client_by_id(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/clients/{client_id}", response_model=ClientResponse)
def update_existing_client(client_id: int, client_data: dict, db: Session = Depends(get_db)):
    client = update_client(db, client_id, client_data)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.delete("/clients/{client_id}", status_code=204)
def delete_existing_client(client_id: int, db: Session = Depends(get_db)):
    client = delete_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
