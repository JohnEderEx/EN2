from sqlalchemy.orm import Session
from app.models.location import Location

class GeolocationService:
    @staticmethod
    def get_nearby_locations(db: Session, latitude: float, longitude: float, category: str = None, radius: int = 5000):
        query = db.query(Location).filter(
            Location.category == category if category else True
        )
        return query.all()
