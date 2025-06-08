# routers/transcription.py

import shutil
from fastapi import APIRouter, UploadFile, File
from faster_whisper import WhisperModel

# Create the router for transcription endpoints
router = APIRouter()

# Load the AI Model
# This will download the model (a few GB) the first time it runs.
# We're using the small, fast "base" model.
stt_model = WhisperModel("base", device="cpu", compute_type="int8")

@router.post("/transcribe-audio/")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Accepts an audio file, transcribes it, and returns the text.
    """
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    segments, _ = stt_model.transcribe(temp_file_path, beam_size=5)
    transcript = " ".join([segment.text for segment in segments])

    return {"transcript": transcript}