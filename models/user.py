#!/usr/bin/python3
"""user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """create the class user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def add_child_attributes(self):
        """
        adds child attributes for child class
        """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
