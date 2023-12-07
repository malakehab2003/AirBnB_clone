#!/usr/bin/python3
""" module for place class """
from models.base_model import BaseModel
from models.place import Place
import unittest
from models import storage
import datetime


class TestPlace(unittest.TestCase):
    """test place"""
    def test_place_attributes(self):
        """test atters"""
        place = Place()
        self.assertEqual(place.name, "")
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_inheritance(self):
        """test inheritance"""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_created_at(self):
        """test created at"""
        place = Place()
        self.assertTrue(type(place.created_at) is datetime.datetime)

    def test_save(self):
        """test save"""
        place = Place()
        first_date = place.updated_at
        place.save()
        second_date = place.updated_at
        self.assertNotEqual(first_date, second_date)

    def test_save_file(self):
        """test save file"""
        place = Place()
        place.save()
        user_id = f"Place.{place.id}"
        self.assertIn(user_id, storage.all())


if __name__ == "__main__":
    unittest.main()
