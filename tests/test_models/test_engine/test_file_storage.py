#!/usr/bin/python3
""" test file model """

import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
"""Test to file_storage"""


class TestFileStorage(unittest.TestCase):
    """class test"""

    def setUp(self):
        """test 1"""
        self.storage = FileStorage()

    def test_file_path_default(self):
        """test 2"""
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects_default(self):
        """test 3"""
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all_returns_dictionary(self):
        """test 4"""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_adds_object_to_objects(self):
        """test 5"""
        obj = BaseModel()
        self.storage.new(obj)
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(obj_key, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[obj_key], obj)

    def test_save_writes_to_file(self):
        """test 6"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        with open(self.storage._FileStorage__file_path, 'r') as file:
            file_data = json.load(file)

        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(obj_key, file_data)
        self.assertEqual(file_data[obj_key], obj.to_dict())

    def test_reload_loads_objects_from_file(self):
        """test 7"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()

        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(obj_key, self.storage._FileStorage__objects)

        reloaded_obj = self.storage._FileStorage__objects[obj_key]
        self.assertEqual(reloaded_obj.__dict__, obj.__dict__)

    def test_path(self):
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_reload(self):
        storage = FileStorage()
        storage.all().clear()
        storage.reload()
        self.assertTrue(len(storage.all()) > 0)


if __name__ == '__main__':
    unittest.main()
