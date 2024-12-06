from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from snowflake.sqlalchemy import URL
from app.config import (
    SNOWFLAKE_USER, SNOWFLAKE_PASSWORD, SNOWFLAKE_ACCOUNT, 
    SNOWFLAKE_WAREHOUSE, SNOWFLAKE_DATABASE, SNOWFLAKE_ROLE, SNOWFLAKE_SCHEMA
)

# Create Snowflake URL
DATABASE_URL = URL(
    account=SNOWFLAKE_ACCOUNT,
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA,
    warehouse=SNOWFLAKE_WAREHOUSE,
    role=SNOWFLAKE_ROLE
)

# Debug print (remove in production)
print(f"Connecting to Snowflake with user: {SNOWFLAKE_USER}")

try:
    # Create engine with Snowflake dialect
    engine = create_engine(DATABASE_URL)
    
    # Create session factory
    SessionLocal = sessionmaker(
        autocommit=False, 
        autoflush=False, 
        bind=engine
    )
    
    # Create declarative base
    Base = declarative_base()
    
    # Optional: Test connection
    def test_connection():
        try:
            with engine.connect() as connection:
                result = connection.execute("SELECT CURRENT_WAREHOUSE()").fetchone()
                print(f"Connected to Snowflake. Current Warehouse: {result[0]}")
        except Exception as conn_error:
            print(f"Connection test failed: {conn_error}")
    
    # Uncomment to test connection during startup
    # test_connection()

except SQLAlchemyError as e:
    print(f"Error creating SQLAlchemy engine: {e}")
    raise

def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()  
    except Exception as e:
        db.rollback()
        print(f"Database rollback due to error: {e}")
        raise
    finally:
        db.close()