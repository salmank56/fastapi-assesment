# 
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.client import Client
from app.schemas.client import ClientCreate
import uuid
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_all_clients(db: Session):
    try:
        return db.query(Client).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching clients")

# def get_client_by_id(db: Session, client_id: str):
#     try:
#         client = db.query(Client).filter(Client.id == client_id).first()
#         if not client:
#             raise HTTPException(status_code=404, detail="Client not found")
#         return client
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Error fetching client")
def get_client_by_id(db: Session, client_id: str):
    try:
        client = db.query(Client).filter(Client.id == client_id).first()
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return client
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        logger.error(f"Error fetching client: {str(e)}")
        raise HTTPException(status_code=500, detail="Error fetching client")

def create_client(db: Session, client: ClientCreate):
    try:
        db_client = Client(id=str(uuid.uuid4()), name=client.name, email=client.email)
        db.add(db_client)
        db.commit()
        db.refresh(db_client)
        return db_client
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error creating client")

def update_client(db: Session, client_id: str, updated_data: dict):
    try:
        client = db.query(Client).filter(Client.id == client_id).first()
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")

        for key, value in updated_data.items():
            setattr(client, key, value)

        db.commit()
        db.refresh(client)

        return client
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error updating client")

def delete_client(db: Session, client_id: str):
    try:
        client = db.query(Client).filter(Client.id == client_id).first()
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")

        db.delete(client)
        db.commit()
        return {"message": "Client successfully deleted"}
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error deleting client")
