#!/usr/bin/python3
""" test place model """

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place
import pycodestyle


class PlaceTest(unittest.TestCase):
    """ Unit Tests class for place tests """

    def test_pep8(self):
        """ Check PEP8 style """
        syntaxis = pycodestyle.StyleGuide(quit=True)
        test = syntaxis.check_files(['models/place.py'])
        self.assertEqual(test.total_errors, 0, "Found style errors")

    def test_subclass(self):
        """test if USer is subclass of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attr(self):
        """test attribute class"""
        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])
        self.assertEqual(type(Place.city_id), str)
        self.assertEqual(type(Place.user_id), str)
        self.assertEqual(type(Place.name), str)
        self.assertEqual(type(Place.description), str)
        self.assertEqual(type(Place.number_rooms), int)
        self.assertEqual(type(Place.number_bathrooms), int)
        self.assertEqual(type(Place.max_guest), int)
        self.assertEqual(type(Place.price_by_night), int)
        self.assertEqual(type(Place.latitude), float)
        self.assertEqual(type(Place.longitude), float)
        self.assertEqual(type(Place.amenity_ids), list)

    def test_instance(self):
        """test instance class"""
        my_place = Place()
        self.assertEqual(my_place.city_id, "")
        self.assertEqual(my_place.user_id, "")
        self.assertEqual(my_place.name, "")
        self.assertEqual(my_place.description, "")
        self.assertEqual(my_place.number_rooms, 0)
        self.assertEqual(my_place.number_bathrooms, 0)
        self.assertEqual(my_place.max_guest, 0)
        self.assertEqual(my_place.price_by_night, 0)
        self.assertEqual(my_place.latitude, 0.0)
        self.assertEqual(my_place.longitude, 0.0)
        self.assertEqual(my_place.amenity_ids, [])
        my_place.city_id = "asd"
        my_place.user_id = "sdf"
        my_place.name = "dfg"
        my_place.description = "fgh"
        my_place.number_rooms = 1
        my_place.number_bathrooms = 2
        my_place.max_guest = 3
        my_place.price_by_night = 4
        my_place.latitude = 1.2
        my_place.longitude = 1.3
        my_place.amenity_ids = [1]
        self.assertEqual(my_place.city_id, "asd")
        self.assertEqual(my_place.user_id, "sdf")
        self.assertEqual(my_place.name, "dfg")
        self.assertEqual(my_place.description, "fgh")
        self.assertEqual(my_place.number_rooms, 1)
        self.assertEqual(my_place.number_bathrooms, 2)
        self.assertEqual(my_place.max_guest, 3)
        self.assertEqual(my_place.price_by_night, 4)
        self.assertEqual(my_place.latitude, 1.2)
        self.assertEqual(my_place.longitude, 1.3)
        self.assertEqual(my_place.amenity_ids, [1])
        self.assertEqual(type(Place.city_id), str)
        self.assertEqual(type(Place.user_id), str)
        self.assertEqual(type(Place.name), str)
        self.assertEqual(type(Place.description), str)
        self.assertEqual(type(Place.number_rooms), int)
        self.assertEqual(type(Place.number_bathrooms), int)
        self.assertEqual(type(Place.max_guest), int)
        self.assertEqual(type(Place.price_by_night), int)
        self.assertEqual(type(Place.latitude), float)
        self.assertEqual(type(Place.longitude), float)
        self.assertEqual(type(Place.amenity_ids), list)
