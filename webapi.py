from fastapi import FastAPI
from api import get_ai_suggestions  # Importing the function from api.py

app = FastAPI()

@app.get("/suggestions/")
def get_suggestions(error_message: str):
    suggestions = get_ai_suggestions(error_message)
    return {"suggestions": suggestions}
