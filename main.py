from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models
import schemas

# Jadvallarni yaratish
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Surxondaryo Water API",
    description="Surxondaryo viloyati ichimlik suvi statistikasi va xarita uchun backend",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# ASOSIY API
# =========================

@app.get("/")
def home():
    return {"message": "Surxondaryo suv sifati va statistika API ishlayapti"}


@app.get("/districts", response_model=list[schemas.DistrictResponse])
def get_districts(db: Session = Depends(get_db)):
    return db.query(models.District).order_by(models.District.id.asc()).all()


@app.get("/districts/{district_id}", response_model=schemas.DistrictResponse)
def get_district(district_id: int, db: Session = Depends(get_db)):
    district = db.query(models.District).filter(models.District.id == district_id).first()
    if district is None:
        raise HTTPException(status_code=404, detail="Tuman topilmadi")
    return district


# =========================
# DISTRICTS SEED
# =========================

@app.get("/seed")
def seed_data(db: Session = Depends(get_db)):
    existing = db.query(models.District).count()
    if existing > 0:
        return {"message": "Bazaga ma'lumot avval kiritilgan"}

    districts_data = [
        {
            "name": "Termiz shahri",
            "ph": 7.1,
            "tds": 300,
            "turbidity": 1.0,
            "chlorine": 0.3,
            "status": "Yaxshi",
            "outage_start": "2026-04-07 09:00:00",
            "outage_end": "2026-04-07 12:00:00",
            "reason": "Quvur ta'mirlash"
        },
        {
            "name": "Denov",
            "ph": 6.8,
            "tds": 500,
            "turbidity": 2.5,
            "chlorine": 0.5,
            "status": "Ortacha",
            "outage_start": "2026-04-08 10:00:00",
            "outage_end": "2026-04-08 14:00:00",
            "reason": "Nasos profilaktikasi"
        },
        {
            "name": "Sherobod",
            "ph": 6.4,
            "tds": 750,
            "turbidity": 4.0,
            "chlorine": 0.8,
            "status": "Yomon",
            "outage_start": "2026-04-09 08:00:00",
            "outage_end": "2026-04-09 16:00:00",
            "reason": "Favqulodda uzilish"
        },
        {
            "name": "Boysun",
            "ph": 7.3,
            "tds": 280,
            "turbidity": 0.9,
            "chlorine": 0.2,
            "status": "Yaxshi",
            "outage_start": "2026-04-10 09:30:00",
            "outage_end": "2026-04-10 11:30:00",
            "reason": "Tarmoq tekshiruvi"
        },
        {
            "name": "Jarqo‘rg‘on",
            "ph": 6.9,
            "tds": 420,
            "turbidity": 1.8,
            "chlorine": 0.4,
            "status": "Ortacha",
            "outage_start": "2026-04-11 13:00:00",
            "outage_end": "2026-04-11 16:00:00",
            "reason": "Rejalashtirilgan texnik ish"
        },
        {
            "name": "Qumqo‘rg‘on",
            "ph": 6.5,
            "tds": 700,
            "turbidity": 3.5,
            "chlorine": 0.7,
            "status": "Yomon",
            "outage_start": "2026-04-12 08:00:00",
            "outage_end": "2026-04-12 15:00:00",
            "reason": "Suv bosimi pastligi"
        },
        {
            "name": "Angor",
            "ph": 7.0,
            "tds": 350,
            "turbidity": 1.2,
            "chlorine": 0.3,
            "status": "Yaxshi",
            "outage_start": "2026-04-13 10:00:00",
            "outage_end": "2026-04-13 12:00:00",
            "reason": "Quvur almashtirish"
        },
        {
            "name": "Muzrabot",
            "ph": 6.7,
            "tds": 480,
            "turbidity": 2.0,
            "chlorine": 0.5,
            "status": "Ortacha",
            "outage_start": "2026-04-14 09:00:00",
            "outage_end": "2026-04-14 13:00:00",
            "reason": "Texnik xizmat"
        },
        {
            "name": "Sariosiyo",
            "ph": 6.3,
            "tds": 800,
            "turbidity": 4.5,
            "chlorine": 0.9,
            "status": "Yomon",
            "outage_start": "2026-04-15 07:30:00",
            "outage_end": "2026-04-15 17:00:00",
            "reason": "Favqulodda ta'mirlash"
        },
        {
            "name": "Uzun",
            "ph": 7.2,
            "tds": 320,
            "turbidity": 1.1,
            "chlorine": 0.3,
            "status": "Yaxshi",
            "outage_start": "2026-04-16 11:00:00",
            "outage_end": "2026-04-16 13:00:00",
            "reason": "Qisqa muddatli uzilish"
        },
        {
            "name": "Bandixon",
            "ph": 6.9,
            "tds": 410,
            "turbidity": 1.7,
            "chlorine": 0.4,
            "status": "Ortacha",
            "outage_start": "2026-04-17 10:00:00",
            "outage_end": "2026-04-17 14:00:00",
            "reason": "Nasos sozlash"
        },
        {
            "name": "Oltinsoy",
            "ph": 7.1,
            "tds": 340,
            "turbidity": 1.0,
            "chlorine": 0.3,
            "status": "Yaxshi",
            "outage_start": "2026-04-18 09:00:00",
            "outage_end": "2026-04-18 11:00:00",
            "reason": "Tizim yangilanishi"
        },
        {
            "name": "Sho‘rchi",
            "ph": 6.6,
            "tds": 620,
            "turbidity": 2.8,
            "chlorine": 0.6,
            "status": "Ortacha",
            "outage_start": "2026-04-19 08:30:00",
            "outage_end": "2026-04-19 12:30:00",
            "reason": "Suv inshooti nazorati"
        },
        {
            "name": "Qiziriq",
            "ph": 6.4,
            "tds": 730,
            "turbidity": 3.9,
            "chlorine": 0.8,
            "status": "Yomon",
            "outage_start": "2026-04-20 07:00:00",
            "outage_end": "2026-04-20 16:00:00",
            "reason": "Quvurdagi nosozlik"
        }
    ]

    for item in districts_data:
        district = models.District(
            name=item["name"],
            ph=item["ph"],
            tds=item["tds"],
            turbidity=item["turbidity"],
            chlorine=item["chlorine"],
            status=item["status"],
            outage_start=item["outage_start"],
            outage_end=item["outage_end"],
            reason=item["reason"]
        )
        db.add(district)

    db.commit()
    return {"message": "Surxondaryo tumanlari bazaga muvaffaqiyatli qo'shildi"}


# =========================
# REGIONAL STATS
# =========================

@app.get("/stats/surxondaryo", response_model=list[schemas.RegionalStatResponse])
def get_surxondaryo_stats(db: Session = Depends(get_db)):
    return (
        db.query(models.RegionalStat)
        .filter(models.RegionalStat.region_name == "Surxondaryo")
        .order_by(models.RegionalStat.year.asc())
        .all()
    )


@app.get("/stats/surxondaryo/projects", response_model=list[schemas.DistrictProjectResponse])
def get_surxondaryo_projects(db: Session = Depends(get_db)):
    return (
        db.query(models.DistrictProject)
        .order_by(models.DistrictProject.year.asc(), models.DistrictProject.district_name.asc())
        .all()
    )


@app.get("/stats/surxondaryo/summary")
def get_surxondaryo_summary(db: Session = Depends(get_db)):
    items = (
        db.query(models.RegionalStat)
        .filter(models.RegionalStat.region_name == "Surxondaryo")
        .all()
    )

    if not items:
        return {"message": "Ma'lumot topilmadi"}

    latest = max(items, key=lambda x: x.year)
    valid_items = [x for x in items if x.drinking_water_coverage_percent is not None]
    first_item = min(valid_items, key=lambda x: x.year) if valid_items else None

    return {
        "region": "Surxondaryo",
        "latest_year": latest.year,
        "latest_coverage_percent": latest.drinking_water_coverage_percent,
        "coverage_growth": round(
            latest.drinking_water_coverage_percent - first_item.drinking_water_coverage_percent, 2
        ) if first_item and latest.drinking_water_coverage_percent is not None else None,
        "total_water_pipes_km": latest.total_water_pipes_km,
        "sewer_pipes_km": latest.sewer_pipes_km,
        "water_facilities_count": latest.water_facilities_count,
    }


# =========================
# REGIONAL STATS SEED
# =========================

@app.get("/seed-stats")
def seed_stats(db: Session = Depends(get_db)):
    existing_regional = db.query(models.RegionalStat).count()
    existing_projects = db.query(models.DistrictProject).count()

    if existing_regional > 0 or existing_projects > 0:
        return {"message": "Statistik ma'lumotlar avval kiritilgan"}

    regional_stats_data = [
        {
            "region_name": "Surxondaryo",
            "year": 2019,
            "drinking_water_coverage_percent": 42.7,
            "household_water_coverage_percent": None,
            "total_water_pipes_km": None,
            "sewer_pipes_km": None,
            "water_facilities_count": None,
            "source_note": "Tarixiy o'sish boshlang'ich nuqtasi"
        },
        {
            "region_name": "Surxondaryo",
            "year": 2024,
            "drinking_water_coverage_percent": 62.9,
            "household_water_coverage_percent": None,
            "total_water_pipes_km": 16273.0,
            "sewer_pipes_km": 572.9,
            "water_facilities_count": 186,
            "source_note": "Viloyat bo'yicha umumiy infratuzilma ko'rsatkichi"
        },
        {
            "region_name": "Surxondaryo",
            "year": 2025,
            "drinking_water_coverage_percent": 66.5,
            "household_water_coverage_percent": 66.5,
            "total_water_pipes_km": 103.7,
            "sewer_pipes_km": 9.3,
            "water_facilities_count": 2,
            "source_note": "2025 yil holati bo'yicha yangi qurilish ko'rsatkichlari"
        }
    ]

    district_projects_data = [
        {
            "district_name": "Bandixon",
            "location_name": "Bahoriston mahallasi",
            "year": 2024,
            "pipes_km": 13.0,
            "households_covered": 750,
            "population_covered": None,
            "water_facilities_count": 1,
            "sewer_pipes_km": None,
            "source_note": "Mahalliy loyiha"
        },
        {
            "district_name": "Termiz",
            "location_name": "Viloyat markazi",
            "year": 2025,
            "pipes_km": None,
            "households_covered": None,
            "population_covered": None,
            "water_facilities_count": None,
            "sewer_pipes_km": None,
            "source_note": "Asosiy loyiha markazi"
        },
        {
            "district_name": "Angor",
            "location_name": "Tuman markazi",
            "year": 2025,
            "pipes_km": None,
            "households_covered": None,
            "population_covered": None,
            "water_facilities_count": None,
            "sewer_pipes_km": None,
            "source_note": "Loyiha hududi"
        },
        {
            "district_name": "Jarqo‘rg‘on",
            "location_name": "Tuman markazi",
            "year": 2025,
            "pipes_km": None,
            "households_covered": None,
            "population_covered": None,
            "water_facilities_count": None,
            "sewer_pipes_km": None,
            "source_note": "Loyiha hududi"
        },
        {
            "district_name": "Qumqo‘rg‘on",
            "location_name": "Tuman markazi",
            "year": 2025,
            "pipes_km": None,
            "households_covered": None,
            "population_covered": None,
            "water_facilities_count": None,
            "sewer_pipes_km": None,
            "source_note": "Loyiha hududi"
        },
        {
            "district_name": "Muzrabot",
            "location_name": "Tuman markazi",
            "year": 2025,
            "pipes_km": None,
            "households_covered": None,
            "population_covered": None,
            "water_facilities_count": None,
            "sewer_pipes_km": None,
            "source_note": "Loyiha hududi"
        },
        {
            "district_name": "Sariosiyo",
            "location_name": "Tuman markazi",
            "year": 2025,
            "pipes_km": None,
            "households_covered": None,
            "population_covered": None,
            "water_facilities_count": None,
            "sewer_pipes_km": None,
            "source_note": "Loyiha hududi"
        },
        {
            "district_name": "Sho‘rchi",
            "location_name": "Tuman markazi",
            "year": 2025,
            "pipes_km": None,
            "households_covered": None,
            "population_covered": None,
            "water_facilities_count": None,
            "sewer_pipes_km": None,
            "source_note": "Loyiha hududi"
        },
        {
            "district_name": "Qiziriq",
            "location_name": "Tuman markazi",
            "year": 2025,
            "pipes_km": None,
            "households_covered": None,
            "population_covered": None,
            "water_facilities_count": None,
            "sewer_pipes_km": None,
            "source_note": "Loyiha hududi"
        },
        {
            "district_name": "Boysun",
            "location_name": "Tuman markazi",
            "year": 2025,
            "pipes_km": None,
            "households_covered": None,
            "population_covered": None,
            "water_facilities_count": None,
            "sewer_pipes_km": None,
            "source_note": "Loyiha hududi"
        },
        {
            "district_name": "Oltinsoy",
            "location_name": "Tuman markazi",
            "year": 2025,
            "pipes_km": None,
            "households_covered": None,
            "population_covered": None,
            "water_facilities_count": None,
            "sewer_pipes_km": None,
            "source_note": "Loyiha hududi"
        }
    ]

    for item in regional_stats_data:
        stat = models.RegionalStat(
            region_name=item["region_name"],
            year=item["year"],
            drinking_water_coverage_percent=item["drinking_water_coverage_percent"],
            household_water_coverage_percent=item["household_water_coverage_percent"],
            total_water_pipes_km=item["total_water_pipes_km"],
            sewer_pipes_km=item["sewer_pipes_km"],
            water_facilities_count=item["water_facilities_count"],
            source_note=item["source_note"]
        )
        db.add(stat)

    for item in district_projects_data:
        project = models.DistrictProject(
            district_name=item["district_name"],
            location_name=item["location_name"],
            year=item["year"],
            pipes_km=item["pipes_km"],
            households_covered=item["households_covered"],
            population_covered=item["population_covered"],
            water_facilities_count=item["water_facilities_count"],
            sewer_pipes_km=item["sewer_pipes_km"],
            source_note=item["source_note"]
        )
        db.add(project)

    db.commit()
    return {"message": "Surxondaryo statistik ma'lumotlari bazaga muvaffaqiyatli qo'shildi"}