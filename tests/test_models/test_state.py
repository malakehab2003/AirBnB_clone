#!/usr/bin/python3
""" module for state class """
from models.base_model import BaseModel
from models.state import State
import unittest
from models import storage
import datetime


class TestState(unittest.TestCase):
    """test state"""
    def test_state_attributes(self):
        """test atters"""
        state = State()
        self.assertEqual(state.name, "")

    def test_state_inheritance(self):
        """test inheritance"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_created_at(self):
        """test created at"""
        state = State()
        self.assertTrue(type(state.created_at) is datetime.datetime)

    def test_save(self):
        """test save"""
        state = State()
        first_date = state.updated_at
        state.save()
        second_date = state.updated_at
        self.assertNotEqual(first_date, second_date)

    def test_save_file(self):
        """test save file"""
        state = State()
        state.save()
        user_id = f"State.{state.id}"
        self.assertIn(user_id, storage.all())


if __name__ == "__main__":
    unittest.main()
