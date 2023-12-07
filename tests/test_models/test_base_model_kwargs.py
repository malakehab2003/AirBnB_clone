#!/usr/bin/python3
"""test passing kwargs"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test task 4"""
    def setUp(self):
        """setup data to use in test"""
        c = "2022-01-01T12:00:00.000000"
        u = "2022-01-02T12:00:00.000000"
        i = "123456"
        self.model_wk = BaseModel(id=i, created_at=c, updated_at = u)
        self.model_wtk = BaseModel()

    def test_id(self):
        """test the id with kwargs"""
        self.assertEqual(self.model_wk.id, "123456")

    def test_created_at(self):
        """test the created_at with kwargs"""
        s = datetime.datetime(2022, 1, 1, 12, 0)
        self.assertEqual(self.model_wk.created_at, s)

    def test_updated_at(self):
        """test the updated_at with kwargs"""
        p = datetime.datetime(2022, 1, 2, 12, 0)
        self.assertEqual(self.model_wk.updated_at, p)

    def test_type(self):
        """ test the created at and updated at type"""
        self.assertIsInstance(self.model_wk.created_at, datetime.datetime)
        self.assertIsInstance(self.model_wtk.created_at, datetime.datetime)
        self.assertIsInstance(self.model_wk.updated_at, datetime.datetime)
        self.assertIsInstance(self.model_wtk.updated_at, datetime.datetime)


if __name__ == "__main__":
    unittest.main()
