import os
from sqlalchemy import  create_engine 
from sqlalchemy.orm import  sessionmaker,declarative_base
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

DATABASE_URL = os.getenv("DATA_BASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False , autoflush = False , bind=engine)

def get_db():
    db = SessionLocal()
    try :
        yield db 
    finally:
        db.close()