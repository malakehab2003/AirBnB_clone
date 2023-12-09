#!/usr/bin/python3
"""
File Storage Module
"""
import json
import os
import sys
from help_functions.storage_helpers import check_if_float


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
                from models.models_dict import all_models
                file_contents = file.read()
                json_loads = json.loads(file_contents)
                self.clear_objects()
                for key, value in json_loads.items():
                    object_init = all_models[value["__class__"]]
                    self.__objects[key] = object_init(**value)

    def clear_objects(self):
        """
        clears all objects
        """
        self.__objects = {}

    def delete_object(self, key):
        """
        delete a specific object
        based on its key
        """
        del self.__objects[key]
        self.save()

    def update_object(self, key, attrib, value):
        """
        update a specific object
        based on its key
        """
        from models.models_dict import all_attrib
        setattr(self.__objects[key], attrib, all_attrib[attrib](value))
        self.save()
