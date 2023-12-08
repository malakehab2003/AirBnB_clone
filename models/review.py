#!/usr/bin/python3
"""Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """create the Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def add_child_attributes(self):
        """
        adds child attributes for child class
        """
        self.place_id = ""
        self.user_id = ""
        self.text = ""
