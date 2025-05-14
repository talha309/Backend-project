from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student
from typing import List
from utils.util import get_db
from validation.validation import Student

router = APIRouter()


@router.post("/create")
def create_student(student:Student, db: Session = Depends(get_db)):
    try:
        new_student = Student(
            name=Student.name,
            dob=Student.dob,
            address=Student.address,
            phone=Student.phone,
            cnic=Student.cnic
        )
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return new_student
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/read")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

@router.get("/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.delete("/{student_id}", status_code=204)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}

@router.put("/{student_id}")
def update_student(student_id: int, student: Student, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.name = student.name
    db.commit()
    return student