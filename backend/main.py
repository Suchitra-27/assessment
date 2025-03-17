from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import asyncio
import os

app = FastAPI()

# Allow Angular frontend to call the API
origins = os.getenv("FRONTEND_URL", "http://localhost:4200").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for response validation
class Group(BaseModel):
    id: int
    first_name: str
    email: str
    nv: int

# Simulated async function to fetch groups
async def fetch_groups():
    await asyncio.sleep(1)  # Simulating async operation
    return [
        {"id": 1, "first_name": "Teresa", "email": "tbarwell@bandcamp.com", "nv": 99},
        {"id": 2, "first_name": "Fernanda", "email": "flstormouth@yandex.ru", "nv": 548},
        {"id": 3, "first_name": "Noble", "email": "nangricz@wikimedia.org", "nv": 350},
        {"id": 4, "first_name": "Aeriell", "email": "cspain3@parallels.com", "nv": 867},
    ]

@app.get("/groups", response_model=List[Group])
async def get_groups():
    """
    Fetch groups from the database (simulated).
    Returns a list of groups.
    """
    return await fetch_groups()

# Run using: uvicorn main:app --reload
