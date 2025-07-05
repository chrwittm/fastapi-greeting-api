from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn #not used, but keeping it to generate the requirements.txt via pipreqs

# Define the FastAPI app
app = FastAPI(
    title="Greeting API",
    description="A simple API that returns a personalized greeting, either via URL query parameters or JSON payload.",
    version="1.0.0"
)

# Enable CORS (for local testing and GitHub Pages deployment)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",              # Local testing
        "http://127.0.0.1:8000",              # Also valid local reference
        "https://chrwittm.github.io",         # GitHub Pages deployment
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define Pydantic model for POST request
class NameRequest(BaseModel):
    name: str

# Pydantic model for response (shared across GET and POST)
class GreetingResponse(BaseModel):
    message: str

# GET endpoint using query parameter
@app.get("/greet", response_model=GreetingResponse, summary="Greet via query parameter")
def greet_get(name: str = Query(default="World", description="The name of the person to greet.")):
    """
    Returns a greeting based on the query parameter 'name'.
    """
    return {"message": f"Hello {name}"}

# POST endpoint using JSON body
@app.post("/greet", response_model=GreetingResponse, summary="Greet via JSON payload")
def greet_post(request: NameRequest):
    """
    Returns a greeting based on the JSON body with a 'name' field.
    """
    return {"message": f"Hello {request.name}"}