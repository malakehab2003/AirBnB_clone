#!/usr/bin/python3
"""test file storage class"""
import json
import os
import unittest

from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Class for Unit Testing FileStorage()

    this class checks for every detail in the class
    """
    file_path = "file.json"

    def clearFile(self):
        """
        deletes the file created for storage
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_base(self):
        """
        checks base case
        """
        self.clearFile()
        storage.clear_objects()
        self.assertTrue(len(storage.all()) == 0)
        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path) as file:
            retrieved_json = file.read()
            self.assertTrue(retrieved_json)
            retrieved_dict = json.loads(retrieved_json)
            last_key = list(retrieved_dict.keys())[-1]
            self.assertDictEqual(retrieved_dict[last_key], my_model.to_dict())

    def test_base_after_reload(self):
        """
        checks if reload works
        """
        self.assertIsNotNone(storage.all())

    def test_no_file(self):
        """
        check no file behavior
        """
        old_storage = storage.all()
        self.clearFile()
        storage.reload()
        self.assertDictEqual(old_storage, storage.all())
