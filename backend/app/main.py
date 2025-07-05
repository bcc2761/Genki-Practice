# main.py - placeholder content
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from fastapi import Request
from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import status
from fastapi import BackgroundTasks
from fastapi import File, UploadFile
from fastapi import Form
from fastapi import WebSocket
from fastapi import WebSocketDisconnect
from fastapi import Cookie
from fastapi import Header
from fastapi import Query
from fastapi import Path
from fastapi import Body
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

class Fruit(BaseModel): 
    name: str
    color: str
    price: float

class Fruits(BaseModel):
    fruits: List[Fruit]
app = FastAPI()

origins = [
    "http://localhost:3000"
    # insert other allowed origins here
    # "https://example.com",    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memory_db = {"fruits": []}

@app.get("/fruits", response_model=Fruits)
def get_fruits():
    return Fruits(fruits=memory_db["fruits"])

@app.post("/fruits", response_model=Fruit)
def add_fruit(fruit: Fruit):
    memory_db["fruits"].append(fruit)
    return fruit

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)