from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PRIVATE_KEY = "6248c7d5-d768-460d-8b03-0e89ccad0a07"

class User(BaseModel):
    username: str

@app.post('/authenticate')
async def authenticate(user: User):
    response = requests.put('https://api.chatengine.io/users/',
        data={
            "username": user.username,
            "secret": user.username,
            "first_name": user.username,
        },
        headers={ "Private-key": PRIVATE_KEY }
    )
    return response.json()
# uvicorn main:app --reload --port 3001