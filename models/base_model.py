#!/usr/bin/pythonf3
"""
base model module, for managing all objects
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if ["created_at", "updated_at"].count(key) == 0:
                        self.__setattr__(key, value)
                    else:
                        self.__setattr__(key, datetime.fromisoformat(value))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.add_child_attributes()
            storage.new(self)

    def add_child_attributes(self):
        """
        placeholder for all child attributes
        """
        pass

    def __str__(self):
        """
        String Representation of class
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        temp_dict = {}
        for key, value in self.__dict__.items():
            temp_dict[key] = value if key not in ["created_at", "updated_at"]\
                else self.__getattribute__(key).isoformat()
        temp_dict['__class__'] = type(self).__name__
        return temp_dict
