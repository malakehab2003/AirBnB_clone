#!/usr/bin/python3
""" module for city class """
from models.base_model import BaseModel
from models.city import City
import unittest
from models import storage
import datetime


class TestCity(unittest.TestCase):
    """test city"""
    def test_city_attributes(self):
        """test atters"""
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")

    def test_city_inheritance(self):
        """test inheritance"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_created_at(self):
        """test created at"""
        city = City()
        self.assertTrue(type(city.created_at) is datetime.datetime)

    def test_save(self):
        """test save"""
        city = City()
        first_date = city.updated_at
        city.save()
        second_date = city.updated_at
        self.assertNotEqual(first_date, second_date)

    def test_save_file(self):
        """test save file"""
        city = City()
        city.save()
        user_id = f"City.{city.id}"
        self.assertIn(user_id, storage.all())


if __name__ == "__main__":
    unittest.main()
