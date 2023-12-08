#!/usr/bin/python3
"""
all models dict
"""

from models.base_model import BaseModel
from models.user import User


all_models = {
    "BaseModel": BaseModel,
    "User": User
}

all_attrib = {
    "email": str,
    "password": str,
    "first_name": str,
    "last_name": str,
    "name": str,
    "state_id": str,
    "city_id": str,
    "user_id": str,
    "description": str,
    "number_rooms": int,
    "number_bathrooms": int,
    "max_guest": int,
    "price_by_night": int,
    "latitude": float,
    "longitude": float,
    "amenity_ids": list[str],
    "place_id": str,
}
