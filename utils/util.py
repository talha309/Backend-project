from config.data_base import SessionLocal 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
