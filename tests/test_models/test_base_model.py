#!/usr/bin/python3
"""test base model"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from os.path import exists
from models import storage


class testBaseModel(unittest.TestCase):
    """test the base model"""
    def test_instanse(self):
        """test new instanse"""
        self.model = BaseModel()
        self.assertTrue(isinstance(self.model, BaseModel))

    def test_id(self):
        """test generation of id"""
        self.model = BaseModel()
        self.assertTrue(isinstance(self.model.id, str))

    def test_change_id(self):
        """test changing of id"""
        self.model = BaseModel()
        self.model2 = BaseModel()
        self.assertTrue(self.model.id != self.model2.id)

    def test_update(self):
        """test update the id"""
        self.model = BaseModel()
        first_id = self.model.updated_at
        self.model.save()
        second_id = self.model.updated_at
        self.assertTrue(first_id != second_id)

    def test_to_dict(self):
        """check to_dict function"""
        self.model = BaseModel()
        self.assertIsInstance(self.model.to_dict(), dict)

    def test_str(self):
        """check the str function"""
        self.m = BaseModel()
        m = self.m
        self.assertEqual(str(self.m),
                         "[BaseModel] ({}) {}".format(m.id, m.__dict__))

    def test_created_at_type(self):
        """check type of created_at and updated at"""
        self.model = BaseModel()
        self.assertTrue(isinstance(self.model.created_at, datetime))
        self.assertTrue(isinstance(self.model.updated_at, datetime))

    def test_to_dict_format(self):
        """check exist in to_dict"""
        self.model = BaseModel()
        model_dict = self.model.to_dict()
        self.assertIn("__class__", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)

    def test_file_exists(self):
        """test the exists of the file"""
        self.model = BaseModel()
        storage.save
        self.assertTrue(exists("instanse.json"))


if __name__ == "__main__":
    unittest.main()
