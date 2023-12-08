#!/usr/bin/python3
"""state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """create the state class"""
    name = ""

    def add_child_attributes(self):
        """
        adds child attributes for child class
        """
        self.name = ""
