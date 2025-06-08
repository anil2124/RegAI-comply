from fastapi import FastAPI
# Import BaseModel from Pydantic
from pydantic import BaseModel
from typing import Optional # We'll use this to mark optional fields

# Create an instance of the FastAPI class
app = FastAPI()

# --- Pydantic Data Model ---
# This class defines the structure of a complaint.
# By inheriting from BaseModel, we get all the Pydantic magic.
class Complaint(BaseModel):
    # We'll start with a few key fields from the PRD
    device_name: str
    defect: str
    symptoms: Optional[str] = None # This field is optional
    # Let's add a placeholder for the raw text from the audio
    raw_transcript: str

# Define a "path operation decorator"
@app.get("/")
def read_root():
    return {"message": "Hello from the RegAI Comply Backend!"}


# --- Complaint Processing Endpoint ---
# We've changed the type annotation from `data: dict` to `complaint: Complaint`
@app.post("/process-complaint")
def process_complaint(complaint: Complaint):
    # Now, FastAPI will automatically validate the incoming data against our
    # Complaint model. If the data is malformed (e.g., device_name is missing),
    # FastAPI will automatically return a helpful error message to the client.

    # We can access the data using dot notation, with full autocomplete!
    print(f"Received complaint for device: {complaint.device_name}")

    return {
        "status": f"Complaint received for device '{complaint.device_name}'",
        "complaint_data": complaint.model_dump() # .model_dump() converts the model to a dict
    }