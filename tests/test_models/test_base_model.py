#!/usr/bin/python3
"""test the basemodel class"""
from datetime import datetime
import unittest
from models.base_model import BaseModel, __doc__
from help_functions.test_helpers import Helpers


class TestBaseModel(unittest.TestCase):
    """
    Class for Unit Testing BaseModel()

    this class checks for every detail in the class
    """

    def test_docs_exists(self):
        """
        check that docs exist
        """
        self.assertIsNotNone(__doc__)
        self.assertNotEqual(__doc__, "")
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertNotEqual(BaseModel.__doc__, "")
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertNotEqual(BaseModel.__init__.__doc__, "")
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertNotEqual(BaseModel.__str__.__doc__, "")
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertNotEqual(BaseModel.save.__doc__, "")
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertNotEqual(BaseModel.to_dict.__doc__, "")

    def test_base(self):
        """
        base test
        """
        helpers = Helpers()
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_dict = {
            "id": my_model.id,
            'created_at': my_model.created_at,
            'updated_at': my_model.updated_at,
            "name": "My First Model",
            "my_number": 89
        }
        helpers.stdout(lambda: print(my_model),
                       f"[BaseModel] ({my_model.id}) {my_dict}\n")
        my_old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(my_model.updated_at, my_old_updated_at)
        my_model_json = my_model.to_dict()
        my_dict = {
            "id": my_model.id,
            'created_at': str(my_model.created_at.isoformat()),
            'updated_at': str(my_model.updated_at.isoformat()),
            "name": "My First Model",
            "my_number": 89,
            "__class__": "BaseModel"
        }
        helpers.stdout(lambda: print(my_model_json),
                       f"{my_dict}\n")
        print("JSON of my_model:")
        my_detailed_dict = {
            "my_number": f"(<class 'int'>) - 89",
            "name": f"(<class 'str'>) - My First Model",
            "__class__": f"(<class 'str'>) - {my_model_json['__class__']}",
            "updated_at": f"(<class 'str'>) - {my_model_json['updated_at']}",
            "id": f"(<class 'str'>) - {my_model_json['id']}",
            "created_at": f"(<class 'str'>) - {my_model_json['created_at']}",
        }
        for key in my_model_json.keys():
            helpers.stdout(lambda: print("\t{}: ({}) - {}"
                                         .format(key,
                                                 type(my_model_json[key]),
                                                 my_model_json[key])),
                           f"\t{key}: {my_detailed_dict[key]}\n")
