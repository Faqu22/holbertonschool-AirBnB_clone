#!/usr/bin/python3
""" test user model """

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
import pycodestyle


class UserTest(unittest.TestCase):
    """ Unit Tests class for user tests """

    def test_subclass(self):
        """test if USer is subclass of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_attr(self):
        """test attribute class"""
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

    def test_instance(self):
        """test instance class"""
        my_user = User()
        self.assertEqual(my_user.email, "")
        self.assertEqual(my_user.password, "")
        self.assertEqual(my_user.first_name, "")
        self.assertEqual(my_user.last_name, "")
        self.assertTrue(isinstance(my_user, BaseModel))

    def test_data(self):
        """test data class"""
        my_user = User()
        my_user.email = "mail@"
        my_user.password = "P4sSw0rD"
        my_user.first_name = "Hol"
        my_user.last_name = "berton"
        self.assertEqual(my_user.email, "mail@")
        self.assertEqual(my_user.password, "P4sSw0rD")
        self.assertEqual(my_user.first_name, "Hol")
        self.assertEqual(my_user.last_name, "berton")
        self.assertTrue(isinstance(my_user, BaseModel))

    def test_pep8_base(self):
        """check PEP8 style"""
        syntaxis = pycodestyle.StyleGuide(quit=True)
        check = syntaxis.check_files(['models/user.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors"
        )
