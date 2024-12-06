# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.crud.client import (
#     get_all_clients,
#     get_client_by_id,
#     create_client,
#     update_client,
#     delete_client,
# )
# from app.schemas.client import ClientCreate, ClientResponse
# from app.db import SessionLocal, get_db
# from fastapi import HTTPException

# router = APIRouter()

# @router.post("/clients", response_model=ClientResponse, status_code=201)
# async def create_new_client(client: ClientCreate, db: Session = Depends(get_db)):
#     try:
#         return create_client(db, client)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @router.get("/clients", response_model=list[ClientResponse])
# def read_clients(db: Session = Depends(get_db)):
#     return get_all_clients(db)

# @router.get("/clients/{client_id}", response_model=ClientResponse)
# def read_client(client_id: int, db: Session = Depends(get_db)):
#     client = get_client_by_id(db, client_id)
#     if not client:
#         raise HTTPException(status_code=404, detail="Client not found")
#     return client

# @router.put("/clients/{client_id}", response_model=ClientResponse)
# def update_existing_client(client_id: int, client_data: dict, db: Session = Depends(get_db)):
#     client = update_client(db, client_id, client_data)
#     if not client:
#         raise HTTPException(status_code=404, detail="Client not found")
#     return client

# @router.delete("/clients/{client_id}", status_code=204)
# def delete_existing_client(client_id: int, db: Session = Depends(get_db)):
#     client = delete_client(db, client_id)
#     if not client:
#         raise HTTPException(status_code=404, detail="Client not found")

from fastapi import APIRouter, Depends, HTTPException
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

# Create a new client
@router.post("/clients", response_model=ClientResponse, status_code=201)
async def create_new_client(client: ClientCreate, db: Session = Depends(get_db)):
    try:
        return create_client(db, client)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating client: {str(e)}")

# Get all clients
@router.get("/clients", response_model=list[ClientResponse])
async def read_clients(db: Session = Depends(get_db)):
    try:
        return get_all_clients(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching clients: {str(e)}")

# Get a client by ID (UUID)
@router.get("/clients/{client_id}", response_model=ClientResponse)
async def read_client(client_id: str, db: Session = Depends(get_db)):
    try:
        client = get_client_by_id(db, client_id)
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return client
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching client: {str(e)}")

@router.put("/clients/{client_id}", response_model=ClientResponse)
def update_existing_client(client_id: str, client_data: ClientUpdate, db: Session = Depends(get_db)):
    try:
        updated_client = update_client(db, client_id, client_data.dict(exclude_unset=True))

        return updated_client
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")


@router.delete("/clients/{client_id}", status_code=204)
async def delete_existing_client(client_id: str, db: Session = Depends(get_db)):
    try:
        client = delete_client(db, client_id)
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return None  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting client: {str(e)}")
