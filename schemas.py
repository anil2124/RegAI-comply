# schemas.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid

# This is our base model. It has the fields that are common
# to both creating and reading complaints.
class ComplaintBase(BaseModel):
    device_name: str
    defect: str
    symptoms: Optional[str] = None
    raw_transcript: str

# This model is used when CREATING a new complaint via the API.
# It inherits all the fields from ComplaintBase.
class ComplaintCreate(ComplaintBase):
    # --- NEW: Add severity field ---
    # It's optional because it might be added manually or by the NLP service.
    severity: Optional[str] = "Normal"


# This is the main model that will be used when READING a complaint
# from the API. It includes all the fields that are stored in the database.
class Complaint(ComplaintBase):
    id: uuid.UUID
    status: str
    # --- NEW: Add severity field ---
    severity: str
    created_at: datetime
    updated_at: datetime

    # Pydantic configuration
    class Config:
        from_attributes = True

