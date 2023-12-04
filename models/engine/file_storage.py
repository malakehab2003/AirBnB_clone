#!/usr/bin/python3
"""
File Storage Module
"""
import json
import os
import sys


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        file_objects = {}
        for key, value in self.__objects.items():
            file_objects[key] = value.to_dict()
        json_dumps = json.dumps(file_objects)
        with open(self.__file_path, "w") as file:
            file.write(json_dumps)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.exists(self.__file_path):
            file_contents = ""
            with open(self.__file_path, "r") as file:
                from models.base_model import BaseModel
                object_dict = {
                    "BaseModel": BaseModel
                }
                file_contents = file.read()
                json_loads = json.loads(file_contents)
                self.__objects = {}
                for key, value in json_loads.items():
                    object_init = object_dict[value["__class__"]]
                    self.__objects[key] = object_init(**value)
