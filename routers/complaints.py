# routers/complaints.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

# Use absolute imports from the project root instead of relative ones
import crud
import schemas
from database import SessionLocal

router = APIRouter()

# --- Database Dependency ---
# We define the get_db dependency here as well, so this module is self-contained.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/complaints/", response_model=schemas.Complaint)
def create_new_complaint(complaint: schemas.ComplaintCreate, db: Session = Depends(get_db)):
    """Creates a new complaint and saves it to the database."""
    return crud.create_complaint(db=db, complaint=complaint)

@router.get("/complaints/", response_model=List[schemas.Complaint])
def read_complaints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieves all complaint records from the database."""
    complaints = crud.get_complaints(db, skip=skip, limit=limit)
    return complaints
