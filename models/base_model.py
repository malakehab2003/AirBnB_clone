#!/usr/bin/python3
"""make Base class"""
import uuid
import datetime
from models import storage


class BaseModel():
    """
    base class to defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        the init method
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            way = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.datetime.strptime(value, way))
                else:
                    setattr(self, key, value)

    def __str__(self):
        """
        [<class name>] (<self.id>) <self.__dict__>
        """
        self.__dict__.pop("__class__", None)
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        update the updated_at date
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        make dict of all data of the instanse
        """
        dict_instanse = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                value = getattr(self, key).isoformat()
                dict_instanse[key] = value
            else:
                dict_instanse[key] = value
        dict_instanse['__class__'] = type(self).__name__
        return dict_instanse
