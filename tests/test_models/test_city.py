#!/usr/bin/python3
""" test city model """

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City
import pycodestyle


class CityTest(unittest.TestCase):
    """ Unit Tests class for city tests """

    def test_pep8(self):
        """ Check PEP8 style """
        syntaxis = pycodestyle.StyleGuide(quit=True)
        test = syntaxis.check_files(['models/city.py'])
        self.assertEqual(test.total_errors, 0, "Found style errors")

    def test_subclass(self):
        """test if USer is subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attr(self):
        """test attribute class"""
        self.assertEqual(City.state_id, "")
        self.assertEqual(City.name, "")
        self.assertIs(type(City.state_id), str)
        self.assertIs(type(City.name), str)

    def test_instance(self):
        """test instance class"""
        my_city = City()
        self.assertEqual(my_city.state_id, "")
        self.assertEqual(my_city.name, "")
        my_city.state_id = "asd"
        my_city.name = "NY"
        self.assertEqual(my_city.state_id, "asd")
        self.assertEqual(my_city.name, "NY")
        self.assertIs(type(my_city.state_id), str)
        self.assertIs(type(my_city.name), str)
        self.assertTrue(isinstance(my_city, BaseModel))
