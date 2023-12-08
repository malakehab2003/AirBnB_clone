#!/usr/bin/python3
"""more tests to basemodel class"""
from datetime import datetime
import unittest
from models.base_model import BaseModel, __doc__
from help_functions.test_helpers import Helpers


class TestBaseModel(unittest.TestCase):
    """
    Class for Unit Testing BaseModel()

    this class checks for every detail in the class
    """

    def test_base_init_kwargs(self):
        """
        kwargs test
        """
        helpers = Helpers()
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model.save()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        my_dict = {
            "id": my_model.id,
            'created_at': my_model.created_at,
            'updated_at': my_model.updated_at,
            "name": "My First Model",
            "my_number": 89
        }
        self.assertEqual(my_new_model.id, my_model.id)
        self.assertEqual(my_new_model.created_at, my_model.created_at)
        self.assertEqual(my_new_model.updated_at, my_model.updated_at)
        self.assertEqual(my_new_model.name, my_model.name)
        self.assertEqual(my_new_model.my_number, my_model.my_number)
        self.assertIsNot(my_new_model, my_model)
        self.assertIsInstance(my_new_model, BaseModel)
        self.assertIsInstance(my_new_model.id, str)
        self.assertIsInstance(my_new_model.created_at, datetime)
        self.assertIsInstance(my_new_model.updated_at, datetime)
        helpers.stdout(lambda: print(my_new_model),
                       f"[BaseModel] ({my_model.id}) {my_dict}\n")
