from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Nom du lieu
    address = Column(String, nullable=False)  # Adresse complète
    latitude = Column(Float, nullable=False)  # Latitude
    longitude = Column(Float, nullable=False)  # Longitude
    category = Column(String, nullable=False)  # Catégorie
