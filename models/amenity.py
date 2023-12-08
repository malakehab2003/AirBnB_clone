#!/usr/bin/python3
"""Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """create the Amenity class"""
    name = ""

    def add_child_attributes(self):
        """
        adds child attributes for child class
        """
        self.name = ""
