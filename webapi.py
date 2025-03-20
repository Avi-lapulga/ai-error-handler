from fastapi import FastAPI
from api import get_ai_suggestions  # Import your function

app = FastAPI()

@app.get("/suggestions/")
def get_suggestions(error_message: str):
    """Return AI-generated suggestions for an error message."""
    suggestions = get_ai_suggestions(error_message)
    return {"suggestions": suggestions}
