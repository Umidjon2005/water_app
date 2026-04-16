from sqlalchemy import Column, Integer, String, Float
from database import Base

class WaterData(Base):
    __tablename__ = "water_data"

    id = Column(Integer, primary_key=True, index=True)
    district = Column(String, index=True)
    location_name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    status = Column(String)
    water_level = Column(Float, nullable=True)