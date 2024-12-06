from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from app.config import SNOWFLAKE_USER, SNOWFLAKE_PASSWORD, SNOWFLAKE_ACCOUNT, SNOWFLAKE_WAREHOUSE, SNOWFLAKE_DATABASE, SNOWFLAKE_ROLE, SNOWFLAKE_SCHEMA


print(f"SNOWFLAKE_USER: {SNOWFLAKE_USER}")
print(f"SNOWFLAKE_PASSWORD: {SNOWFLAKE_PASSWORD}")
print(f"SNOWFLAKE_ACCOUNT: {SNOWFLAKE_ACCOUNT}")

DATABASE_URL = (
    f"snowflake://{SNOWFLAKE_USER}:{SNOWFLAKE_PASSWORD}@{SNOWFLAKE_ACCOUNT}/"
    f"?warehouse={SNOWFLAKE_WAREHOUSE}&database={SNOWFLAKE_DATABASE}&role={SNOWFLAKE_ROLE}&schema={SNOWFLAKE_SCHEMA}"
)

print(DATABASE_URL, 'databse url')

try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
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
        raise e
    finally:
        db.close()  