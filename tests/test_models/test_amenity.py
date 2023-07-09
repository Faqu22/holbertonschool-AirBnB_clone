#!/usr/bin/python3
""" test amenity model """

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
import pycodestyle


class AmenityTest(unittest.TestCase):
    """ Unit Tests class for amenity tests """

    def test_pep8(self):
        """ Check PEP8 style """
        syntaxis = pycodestyle.StyleGuide(quit=True)
        test = syntaxis.check_files(['models/amenity.py'])
        self.assertEqual(test.total_errors, 0, "Found style errors")

    def test_subclass(self):
        """test if USer is subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attr(self):
        """test attribute class"""
        self.assertEqual(Amenity.name, "")
        self.assertIs(type(Amenity.name), str)

    def test_instance(self):
        """test instance class"""
        my_amenity = Amenity()
        self.assertEqual(my_amenity.name, "")
        my_amenity.name = "amen"
        self.assertEqual(my_amenity.name, "amen")
        self.assertIs(type(my_amenity.name), str)
