from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class DistrictResponse(BaseModel):
    id: int
    name: str
    ph: float
    tds: int
    turbidity: float
    chlorine: float
    status: str
    outage_start: datetime
    outage_end: datetime
    reason: str

    class Config:
        from_attributes = True


class RegionalStatResponse(BaseModel):
    id: int
    region_name: str
    year: int
    drinking_water_coverage_percent: Optional[float] = None
    household_water_coverage_percent: Optional[float] = None
    total_water_pipes_km: Optional[float] = None
    sewer_pipes_km: Optional[float] = None
    water_facilities_count: Optional[int] = None
    source_note: Optional[str] = None

    class Config:
        from_attributes = True


class DistrictProjectResponse(BaseModel):
    id: int
    district_name: str
    location_name: Optional[str] = None
    year: Optional[int] = None
    pipes_km: Optional[float] = None
    households_covered: Optional[int] = None
    population_covered: Optional[int] = None
    water_facilities_count: Optional[int] = None
    sewer_pipes_km: Optional[float] = None
    source_note: Optional[str] = None

    class Config:
        from_attributes = True