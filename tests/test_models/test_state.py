#!/usr/bin/python3
""" test state model """

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
import pycodestyle


class UserTest(unittest.TestCase):
    """ Unit Tests class for state tests """

    def test_pep8(self):
        """ Check PEP8 style """
        syntaxis = pycodestyle.StyleGuide(quit=True)
        test = syntaxis.check_files(['models/state.py'])
        self.assertEqual(test.total_errors, 0, "Found style errors")

    def test_subclass(self):
        """test if USer is subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_attr(self):
        """test attribute class"""
        self.assertEqual(State.name, "")
        self.assertIs(type(State.name), str)

    def test_instance(self):
        """test instance class"""
        my_state = State()
        self.assertEqual(my_state.name, "")
        my_state.name = "amen"
        self.assertEqual(my_state.name, "amen")
        self.assertIs(type(my_state.name), str)
