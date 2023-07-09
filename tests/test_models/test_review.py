#!/usr/bin/python3
""" test review model """

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review
import pycodestyle


class ReviewTest(unittest.TestCase):
    """ Unit Tests class for review tests """

    def test_pep8(self):
        """ Check PEP8 style """
        syntaxis = pycodestyle.StyleGuide(quit=True)
        test = syntaxis.check_files(['models/review.py'])
        self.assertEqual(test.total_errors, 0, "Found style errors")

    def test_subclass(self):
        """test if USer is subclass of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attr(self):
        """test attribute class"""
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")
        self.assertIs(type(Review.place_id), str)
        self.assertIs(type(Review.user_id), str)
        self.assertIs(type(Review.text), str)

    def test_instance(self):
        """test instance class"""
        my_review = Review()
        self.assertEqual(my_review.place_id, "")
        self.assertEqual(my_review.user_id, "")
        self.assertEqual(my_review.text, "")
        my_review.place_id = "asd"
        my_review.user_id = "sdf"
        my_review.text = "dfg"
        self.assertEqual(my_review.place_id, "asd")
        self.assertEqual(my_review.user_id, "sdf")
        self.assertEqual(my_review.text, "dfg")
        self.assertIs(type(my_review.place_id), str)
        self.assertIs(type(my_review.user_id), str)
        self.assertIs(type(my_review.text), str)
        self.assertTrue(isinstance(my_review, BaseModel))
