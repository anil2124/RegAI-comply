# models.py

from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

from database import Base

class Complaint(Base):
    """
    This class defines the 'complaints' table in our database using SQLAlchemy.
    Each attribute of this class represents a column in the table.
    """
    __tablename__ = "complaints"

    # --- Column Definitions ---
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    device_name = Column(String, index=True)
    defect = Column(String, index=True)
    symptoms = Column(String, nullable=True)
    raw_transcript = Column(Text)
    status = Column(String, default="OPEN")

    # --- NEW: Add severity column ---
    # This will store the AI-classified severity of the complaint.
    severity = Column(String, default="Normal")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
