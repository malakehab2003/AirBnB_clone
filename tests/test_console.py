#!/usr/bin/python3
"""
HBNB Console Test Module
"""

from io import StringIO
import unittest
from unittest.mock import patch
from console import HBNBCommand, __doc__
from help_functions.helpers import Helpers


class TestHBNBCommand(unittest.TestCase):
    """
    Class for Unit Testing HBNBCommand()

    this class checks for every detail in the class
    """

    def test_docs(self):
        """
        check if docs exist
        """
        self.assertIsNotNone(__doc__)
        self.assertNotEqual(__doc__, "")
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertNotEqual(HBNBCommand.__doc__, "")
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertNotEqual(HBNBCommand.do_quit.__doc__, "")
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertNotEqual(HBNBCommand.do_EOF.__doc__, "")
        self.assertIsNotNone(HBNBCommand.help_quit.__doc__)
        self.assertNotEqual(HBNBCommand.help_quit.__doc__, "")
        self.assertIsNotNone(HBNBCommand.help_EOF.__doc__)
        self.assertNotEqual(HBNBCommand.help_EOF.__doc__, "")

    def test_base(self):
        """
        test console
        """
        console = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(console.onecmd('test'))
        self.assertEqual('Testing!!!!\n', fakeOutput.getvalue())
        l = console.precmd('exit')
        r = console.onecmd(l)
        r = console.postcmd(r, l)
        self.assertFalse(r)
