from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a "path operation decorator"
# This tells FastAPI that the function below is responsible for handling
# requests that go to the URL "/" using a GET method.
@app.get("/")
def read_root():
    # This is the response that will be sent back to the browser
    return {"message": "Hello from the RegAI Comply Backend!"}

# A new endpoint for our future complaint processing
@app.post("/process-complaint")
def process_complaint(data: dict):
    # For now, we just pretend to process the data and send it back.
    # In the future, this is where the NLP magic will happen!
    print("Received data:", data)
    return {
        "status": "Complaint received",
        "processed_data": data
    }