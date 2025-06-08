# crud.py

from sqlalchemy.orm import Session
import models
import schemas
import uuid

def get_complaint_by_id(db: Session, complaint_id: uuid.UUID):
    """
    Retrieves a single complaint from the database by its ID.
    """
    return db.query(models.Complaint).filter(models.Complaint.id == complaint_id).first()

def create_complaint(db: Session, complaint: schemas.ComplaintCreate):
    """
    Creates a new complaint record in the database.
    """
    db_complaint = models.Complaint(**complaint.model_dump())
    db.add(db_complaint)
    db.commit()
    db.refresh(db_complaint)
    return db_complaint

def get_complaints(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieves all complaint records from the database.
    """
    # Sort by creation date descending to show newest first
    return db.query(models.Complaint).order_by(models.Complaint.created_at.desc()).offset(skip).limit(limit).all()
