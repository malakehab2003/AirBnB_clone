#!/usr/bin/python3
""" module for review class """
from models.base_model import BaseModel
from models.review import Review
import unittest
from models import storage
import datetime


class TestReview(unittest.TestCase):
    """test review"""
    def test_review_attributes(self):
        """test atters"""
        review = Review()
        self.assertEqual(review.text, "")
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")

    def test_review_inheritance(self):
        """test inheritance"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_created_at(self):
        """test created at"""
        review = Review()
        self.assertTrue(type(review.created_at) is datetime.datetime)

    def test_save(self):
        """test save"""
        review = Review()
        first_date = review.updated_at
        review.save()
        second_date = review.updated_at
        self.assertNotEqual(first_date, second_date)

    def test_save_file(self):
        """test save file"""
        review = Review()
        review.save()
        user_id = f"Review.{review.id}"
        self.assertIn(user_id, storage.all())


if __name__ == "__main__":
    unittest.main()
