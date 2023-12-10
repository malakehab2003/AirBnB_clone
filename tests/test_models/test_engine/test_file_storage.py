#!/usr/bin/python3
"""test file storage"""
from models.base_model import BaseModel
import unittest
from models import storage
from os.path import exists
from os import remove
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """test file storage"""

    def setUp(self):
        """set up data to use"""
        self.storage = FileStorage()

    def test_exist(self):
        """test save"""
        self.mod = BaseModel()
        self.assertIn("BaseModel." + self.mod.id, storage.all().keys())

    def test_remove(self):
        """remove file"""
        remove("file.json")
        self.assertFalse(exists("file.json"))

    def test_all(self):
        """test all function"""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """test new function"""
        model = BaseModel()
        self.storage.new(model)
        self.assertIn("BaseModel.{}".format(model.id), self.storage.all())

    def test_save_reload(self):
        """ test reload function"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertIn("BaseModel.{}".format(model.id), new_storage.all())


if __name__ == "__main__":
    unittest.main()
