from sqlalchemy import Column, Integer, String, Float, Text, TIMESTAMP
from database import Base

class District(Base):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    ph = Column(Float, nullable=False)
    tds = Column(Integer, nullable=False)
    turbidity = Column(Float, nullable=False)
    chlorine = Column(Float, nullable=False)
    status = Column(String(50), nullable=False)
    outage_start = Column(TIMESTAMP, nullable=False)
    outage_end = Column(TIMESTAMP, nullable=False)
    reason = Column(Text, nullable=False)

class RegionalStat(Base):
    __tablename__ = "regional_stats"

    id = Column(Integer, primary_key=True, index=True)
    region_name = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    drinking_water_coverage_percent = Column(Float, nullable=True)
    household_water_coverage_percent = Column(Float, nullable=True)
    total_water_pipes_km = Column(Float, nullable=True)
    sewer_pipes_km = Column(Float, nullable=True)
    water_facilities_count = Column(Integer, nullable=True)
    source_note = Column(Text, nullable=True)


class DistrictProject(Base):
    __tablename__ = "district_projects"

    id = Column(Integer, primary_key=True, index=True)
    district_name = Column(String(100), nullable=False)
    location_name = Column(String(150), nullable=True)
    year = Column(Integer, nullable=True)
    pipes_km = Column(Float, nullable=True)
    households_covered = Column(Integer, nullable=True)
    population_covered = Column(Integer, nullable=True)
    water_facilities_count = Column(Integer, nullable=True)
    sewer_pipes_km = Column(Float, nullable=True)
    source_note = Column(Text, nullable=True)