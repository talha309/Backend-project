from fastapi import APIRouter, Depends
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from models.student_model import Login
from config.data_base import get_db

router = APIRouter()

class Login(BaseModel):
    email: EmailStr
    password: str

@router.post("/register")
def register_user(user: Login, db:Session = Depends(get_db)):  # renamed parameter for clarity
    try:
        new_user = Login(
            email=Login.email,
            password=Login.password  # ⚠️ You should hash passwords before storing them!
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {
            "data": {
                "email": new_user.email,
                "password":new_user.password
            },
            "message": "User successfully registered",
            "status": "ok"
        }

    except Exception as e:
        return {
            "message": f"An error occurred: {str(e)}"
        }
