#!/usr/bin/python3
"""
user model module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User Class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def add_child_attributes(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
