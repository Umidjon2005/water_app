from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models

app = FastAPI()

try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    print("DB ERROR:", e)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()