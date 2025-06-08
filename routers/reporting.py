# routers/reporting.py

import uuid
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

# Use absolute imports from the project root
import crud
from services import report_generator
from database import SessionLocal

router = APIRouter()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/complaints/{complaint_id}/report", response_class=HTMLResponse)
def get_complaint_report(complaint_id: uuid.UUID, db: Session = Depends(get_db)):
    """
    Generates and returns an HTML report for a specific complaint.
    """
    # 1. Fetch the specific complaint from the database using its ID
    complaint = crud.get_complaint_by_id(db, complaint_id=complaint_id)
    
    # 2. Handle case where complaint is not found
    if complaint is None:
        raise HTTPException(status_code=404, detail="Complaint not found")
        
    # 3. Generate the HTML content using our service
    html_content = report_generator.generate_html_report(complaint)
    
    # 4. Return the HTML content as a response
    return HTMLResponse(content=html_content)
