from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.student_model import Login as UserModel
from config.data_base import get_db
from validation.validation import Login

router = APIRouter()


@router.post("/register")
def register_user(user: Login, db: Session = Depends(get_db)):
    try:
        new_user = UserModel(
            email=Login.email,
            password=Login.password  # Hash this password!
        )
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return {
            "data": {"email": new_user.email},  # Don't return password
            "message": "User successfully registered",
            "status": "ok"
        }
    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}

@router.post("/login")
def login_user(user: Login, db: Session = Depends(get_db)):
    try:
        db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
        if not db_user:
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        # Add password verification logic here
        # if not verify_password(user.password, db_user.password):
        #     raise HTTPException(status_code=401, detail="Invalid credentials")
        
        return {"message": "Login successful", "status": "ok"}
    except HTTPException:
        raise
    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}
