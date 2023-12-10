#!/usr/bin/python3
"""file serialization-deserialization"""
import json
from os.path import exists


class FileStorage():
    """
    class to serialization-deserialization data of each instanse
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        return the dict of all data
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        dict_items = {}
        for key, value in self.__objects.items():
            dict_items[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(dict_items, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if exists(self.__file_path):
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review
            class_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
            }
            with open(self.__file_path, 'r') as file:
                dict_file = json.load(file)
                for key, value in dict_file.items():
                    needed_class = value["__class__"]
                    self.__objects[key] = class_dict[needed_class](**value)
