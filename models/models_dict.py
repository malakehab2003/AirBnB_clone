#!/usr/bin/python3
"""
all models dict
"""

from models.base_model import BaseModel
from models.user import User
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

all_models = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review,
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
    "amenity_ids": list,
    "place_id": str,
    }
