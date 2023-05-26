from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

origins = [
    "http://localhost:3000",  # Add your frontend URL here
    # You can add additional frontend URLs if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class Item(BaseModel):
    key: str
    value: str

@app.get("/get/{key}")
def get_value(key: str):
    try:
      return {"key": key, "value": '1'}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error occurred during retrieval")
 