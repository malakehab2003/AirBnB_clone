#!/usr/bin/python3
"""test user class"""
import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
    """test user class"""
    def test_user_attributes(self):
        """test atters"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_inheritance(self):
        """test inhertanse"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_add_email(self):
        """add email"""
        user = User()
        user.email = "test@gmail.com"
        self.assertEqual(user.email, "test@gmail.com")

    def test_password_email(self):
        """add password"""
        user = User()
        user.password = "12345"
        self.assertEqual(user.password, "12345")

    def test_add_first_name(self):
        """add first name"""
        user = User()
        user.first_name = "user"
        self.assertEqual(user.first_name, "user")

    def test_add_last_name(self):
        """add last name"""
        user = User()
        user.last_name = "user"
        self.assertEqual(user.last_name, "user")

    def test_save(self):
        """test save"""
        user = User()
        user.save()
        user_id = f"User.{user.id}"
        self.assertIn(user_id, storage.all())

    def test_updated_at(self):
        """test updated_at in user"""
        user = User()
        first_date = user.updated_at
        user.save()
        second_date = user.updated_at
        self.assertFalse(first_date == second_date)


if __name__ == "__main__":
    unittest.main()
