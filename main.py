from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
import models

app = FastAPI(title="Water Backend API")

# Jadval yaratish
Base.metadata.create_all(bind=engine)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # keyin xohlasang frontend domenini qo'yamiz
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Water backend ishlayapti"}

@app.get("/health")
def health():
    return {"status": "ok"}