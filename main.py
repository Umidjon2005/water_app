from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Backend ishlayapti"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/water")
def create_water(name: str, status: str, db: Session = Depends(get_db)):
    water = models.Water(name=name, status=status)
    db.add(water)
    db.commit()
    db.refresh(water)
    return water

@app.get("/water")
def get_waters(db: Session = Depends(get_db)):
    return db.query(models.Water).all()