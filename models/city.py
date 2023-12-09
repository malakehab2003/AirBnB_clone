#!/usr/bin/python3
"""city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """create the city model

    Attributes:
        state_id (str): The state id.
    """
    state_id = ""
    name = ""
