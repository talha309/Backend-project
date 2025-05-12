from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    dob = Column(DateTime, nullable=False)  # Date of Birth
    address = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(15), nullable=False, unique=True)
    cnic = Column(String(15), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


