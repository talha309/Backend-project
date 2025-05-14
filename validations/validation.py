from pydantic import BaseModel, EmailStr
from datetime import datetime

class Student(BaseModel):
    name: str
    dob: datetime
    address: str
    phone: str
    cnic: str

class Login(BaseModel):
    email: EmailStr
    password: str
