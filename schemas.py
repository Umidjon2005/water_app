from pydantic import BaseModel
from typing import Optional

class WaterDataBase(BaseModel):
    district: str
    location_name: str
    latitude: float
    longitude: float
    status: str
    water_level: Optional[float] = None

class WaterDataCreate(WaterDataBase):
    pass

class WaterDataOut(WaterDataBase):
    id: int

    class Config:
        from_attributes = True