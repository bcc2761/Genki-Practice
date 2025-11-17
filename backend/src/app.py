from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware # to handle CORS, allowing frontend to communicate with backend
from clerk_backend_api import Clerk
import os

clerk_sdk = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
