from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.geolocation_service import GeolocationService

location_routes = Blueprint("locations", __name__)

@location_routes.route("/locations/nearby", methods=["GET"])
def get_nearby_locations():
    latitude = request.args.get("latitude", type=float)
    longitude = request.args.get("longitude", type=float)
    category = request.args.get("category", type=str)
    radius = request.args.get("radius", default=5000, type=int)

    if not latitude or not longitude:
        return jsonify({"error": "Latitude et longitude sont requis"}), 400

    db: Session = get_db()
    locations = GeolocationService.get_nearby_locations(db, latitude, longitude, category, radius)

    return jsonify([
        {"id": loc.id, "name": loc.name, "address": loc.address, 
         "latitude": loc.latitude, "longitude": loc.longitude}
        for loc in locations
    ])
