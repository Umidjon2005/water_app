from sqlalchemy import Column, Integer, String, Float, Text
from database import Base

class WaterLocation(Base):
    __tablename__ = "water_locations"

    id = Column(Integer, primary_key=True, index=True)
    district = Column(String, nullable=False)
    location_name = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    water_level = Column(Float, nullable=True)
    description = Column(Text, nullable=True)