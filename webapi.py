from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ai_error_handler.api import generate_suggestion  # Correct import

app = FastAPI()

class ErrorRequest(BaseModel):
    error: str

@app.post("/suggestions/")
def get_suggestion(error_request: ErrorRequest):
    """Process error messages and return AI-generated suggestions."""
    suggestion = generate_suggestion(error_request.error)  # Call the function correctly
    if not suggestion:
        raise HTTPException(status_code=500, detail="AI could not generate a suggestion.")
    return {"suggestion": suggestion}
