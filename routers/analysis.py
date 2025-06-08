# routers/analysis.py

from fastapi import APIRouter
from pydantic import BaseModel

# Import our NLP service
from services import nlp_analyzer

router = APIRouter()

# Define the data shape for our request body using Pydantic
class TranscriptRequest(BaseModel):
    text: str

@router.post("/analyze-transcript/")
def analyze_transcript_endpoint(request: TranscriptRequest):
    """
    Accepts a transcript text and returns extracted entities.
    """
    # Call the analyze_transcript function from our service
    extracted_entities = nlp_analyzer.analyze_transcript(request.text)
    return extracted_entities
