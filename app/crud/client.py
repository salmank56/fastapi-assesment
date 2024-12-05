from sqlalchemy.orm import Session
from app.models.client import Client
from app.schemas.client import ClientCreate

def get_all_clients(db: Session):
    return db.query(Client).all()

def get_client_by_id(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def create_client(db: Session, client: ClientCreate):
    db_client = Client(name=client.name, email=client.email)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def update_client(db: Session, client_id: int, updated_data: dict):
    client = db.query(Client).filter(Client.id == client_id).first()
    if client:
        for key, value in updated_data.items():
            setattr(client, key, value)
        db.commit()
        db.refresh(client)
    return client

def delete_client(db: Session, client_id: int):
    client = db.query(Client).filter(Client.id == client_id).first()
    if client:
        db.delete(client)
        db.commit()
    return client
