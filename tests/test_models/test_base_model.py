#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from help_functions.helpers import Helpers

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
        my_model.name = "My First Model"
        my_model.my_number = 89
        helpers.stdout(lambda:print(my_model),(f"[BaseModel] ({my_model.id}) " 
                "{"
                f"'id': '{my_model.id}', "
                f"'created_at': {my_model.created_at}, "
                f"'updated_at': {my_model.updated_at}, "
                f"'name': 'My First Model', "
                f"'my_number': 89"
                "}"))
        """ my_model.save()
        print(my_model)
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key])) """