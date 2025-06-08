# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine

# Import our router modules
# --- ADD 'reporting' TO THIS LINE ---
from routers import complaints, transcription, analysis, reporting

# This command ensures that the database tables are created
models.Base.metadata.create_all(bind=engine)

# Create the main FastAPI application instance
app = FastAPI()

# Add CORS middleware
origins = [
    "http://localhost",
    "http://localhost:5173",
    "null",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers from our modules
app.include_router(complaints.router)
app.include_router(transcription.router)
app.include_router(analysis.router)
# --- ADD THIS LINE TO INCLUDE THE NEW ROUTER ---
app.include_router(reporting.router)


@app.get("/")
def read_root():
    return {"status": "RegAI Comply Backend is running"}
