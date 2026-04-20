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


@app.get("/locations")
def get_locations(db: Session = Depends(get_db)):
    try:
        locations = db.query(models.WaterLocation).all()
        return [
            {
                "id": item.id,
                "district": item.district,
                "location_name": item.location_name,
                "latitude": item.latitude,
                "longitude": item.longitude,
                "status": item.status,
                "water_level": item.water_level,
                "description": item.description,
            }
            for item in locations
        ]
    except Exception as e:
        return {"error": str(e)}


@app.get("/locations/add")
def add_location(
    district: str,
    location_name: str,
    latitude: float,
    longitude: float,
    status: str,
    water_level: float = 0,
    description: str = "",
    db: Session = Depends(get_db),
):
    try:
        item = models.WaterLocation(
            district=district,
            location_name=location_name,
            latitude=latitude,
            longitude=longitude,
            status=status,
            water_level=water_level,
            description=description,
        )
        db.add(item)
        db.commit()
        db.refresh(item)

        return {
            "id": item.id,
            "district": item.district,
            "location_name": item.location_name,
            "latitude": item.latitude,
            "longitude": item.longitude,
            "status": item.status,
            "water_level": item.water_level,
            "description": item.description,
        }
    except Exception as e:
        db.rollback()
        return {"error": str(e)}


@app.get("/locations/{location_id}")
def get_location(location_id: int, db: Session = Depends(get_db)):
    try:
        item = db.query(models.WaterLocation).filter(
            models.WaterLocation.id == location_id
        ).first()

        if not item:
            return {"error": "Topilmadi"}

        return {
            "id": item.id,
            "district": item.district,
            "location_name": item.location_name,
            "latitude": item.latitude,
            "longitude": item.longitude,
            "status": item.status,
            "water_level": item.water_level,
            "description": item.description,
        }
    except Exception as e:
        return {"error": str(e)}


@app.put("/locations/{location_id}")
def update_location(
    location_id: int,
    district: str,
    location_name: str,
    latitude: float,
    longitude: float,
    status: str,
    water_level: float = 0,
    description: str = "",
    db: Session = Depends(get_db),
):
    try:
        item = db.query(models.WaterLocation).filter(
            models.WaterLocation.id == location_id
        ).first()

        if not item:
            return {"error": "Topilmadi"}

        item.district = district
        item.location_name = location_name
        item.latitude = latitude
        item.longitude = longitude
        item.status = status
        item.water_level = water_level
        item.description = description

        db.commit()
        db.refresh(item)

        return {
            "message": "Yangilandi",
            "id": item.id,
            "district": item.district,
            "location_name": item.location_name,
            "latitude": item.latitude,
            "longitude": item.longitude,
            "status": item.status,
            "water_level": item.water_level,
            "description": item.description,
        }
    except Exception as e:
        db.rollback()
        return {"error": str(e)}


@app.delete("/locations/{location_id}")
def delete_location(location_id: int, db: Session = Depends(get_db)):
    try:
        item = db.query(models.WaterLocation).filter(
            models.WaterLocation.id == location_id
        ).first()

        if not item:
            return {"error": "Topilmadi"}

        db.delete(item)
        db.commit()

        return {"message": "O‘chirildi"}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}


@app.get("/statistics")
def get_statistics(db: Session = Depends(get_db)):
    try:
        locations = db.query(models.WaterLocation).all()

        total = len(locations)
        good = len([x for x in locations if x.status.lower() == "good"])
        medium = len([x for x in locations if x.status.lower() == "medium"])
        bad = len([x for x in locations if x.status.lower() == "bad"])

        levels = [x.water_level for x in locations if x.water_level is not None]
        avg_level = sum(levels) / len(levels) if levels else 0

        return {
            "total_locations": total,
            "good_count": good,
            "medium_count": medium,
            "bad_count": bad,
            "average_water_level": avg_level,
        }
    except Exception as e:
        return {"error": str(e)}