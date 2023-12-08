#!/usr/bin/python3
""" module for amenity class """
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
from models import storage
import datetime


class TestAmenity(unittest.TestCase):
    """test amenity"""
    def test_amenity_attributes(self):
        """test atters"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_inheritance(self):
        """test inheritance"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_created_at(self):
        """test created at"""
        amenity = Amenity()
        self.assertTrue(type(amenity.created_at) is datetime.datetime)

    def test_save(self):
        """test save"""
        amenity = Amenity()
        first_date = amenity.updated_at
        amenity.save()
        second_date = amenity.updated_at
        self.assertNotEqual(first_date, second_date)

    def test_save_file(self):
        """test save file"""
        amenity = Amenity()
        amenity.save()
        user_id = f"Amenity.{amenity.id}"
        self.assertIn(user_id, storage.all())


if __name__ == "__main__":
    unittest.main()
