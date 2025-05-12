from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os 

load_dotenv()
DATABASE_URL = os.getenv('DATA_BASE_URL')

engine = create_engine(DATABASE_URL)
Sessionlocal = sessionmaker (autoflush=False,autocommit=False,bind=engine)