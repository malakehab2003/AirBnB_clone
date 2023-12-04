#!/usr/bin/python3
"""Unittest for get_element
"""
import unittest

from help_functions.helpers import Helpers


class TestHelpers(unittest.TestCase):
    """
    Class for Unit Testing Helpers()

    this class checks for every detail in the class
    """

    def test_docs_exists(self):
        """
        check that docs exist
        """
        self.assertIsNotNone(__doc__)
        self.assertNotEqual(__doc__, "")
        self.assertIsNotNone(Helpers.__doc__)
        self.assertNotEqual(Helpers.__doc__, "")
        self.assertIsNotNone(Helpers.stdout.__doc__)
        self.assertNotEqual(Helpers.stdout.__doc__, "")
