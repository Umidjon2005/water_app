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
    return {
        "id": water.id,
        "name": water.name,
        "status": water.status
    }

@app.get("/water")
def get_waters(db: Session = Depends(get_db)):
    waters = db.query(models.Water).all()
    return [
        {
            "id": w.id,
            "name": w.name,
            "status": w.status
        }
        for w in waters
    ]