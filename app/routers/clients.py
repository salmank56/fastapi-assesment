from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud.client import (
    get_all_clients,
    get_client_by_id,
    create_client,
    update_client,
    delete_client,
)
from app.schemas.client import ClientCreate, ClientResponse, ClientUpdate
from app.db import get_db

router = APIRouter()

# Create client
@router.post("/clients", response_model=ClientResponse, status_code=201)
async def create_new_client(client: ClientCreate, db: Session = Depends(get_db)):
    try:
        return create_client(db, client)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error creating client")

# get all clients
@router.get("/clients", response_model=list[ClientResponse])
async def read_clients(db: Session = Depends(get_db)):
    try:
        return get_all_clients(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching clients")

# get client by id
@router.get("/clients/{client_id}", response_model=ClientResponse)
async def read_client(client_id: str, db: Session = Depends(get_db)):
    try:
        client = get_client_by_id(db, client_id)
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return client
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        print(e, "error")
        raise HTTPException(status_code=404, detail="Error fetching client")

@router.put("/clients/{client_id}", response_model=ClientResponse)
async def update_existing_client(client_id: str, client_data: ClientUpdate, db: Session = Depends(get_db)):
    try:
        updated_client = update_client(db, client_id, client_data.dict(exclude_unset=True))
        if not updated_client:
            raise HTTPException(status_code=404, detail="Client not found")
        return updated_client
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error updating client")

@router.delete("/clients/{client_id}", status_code=204)
async def delete_existing_client(client_id: str, db: Session = Depends(get_db)):
    try:
        client = delete_client(db, client_id)
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return None
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=404, detail="Error deleting client")
