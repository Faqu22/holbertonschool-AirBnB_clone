import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
"""Test to file_storage"""


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_file_path_default(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects_default(self):
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all_returns_dictionary(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_adds_object_to_objects(self):
        obj = BaseModel()
        self.storage.new(obj)
        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(obj_key, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[obj_key], obj)

    def test_save_writes_to_file(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        with open(self.storage._FileStorage__file_path, 'r') as file:
            file_data = json.load(file)

        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(obj_key, file_data)
        self.assertEqual(file_data[obj_key], obj.to_dict())

    def test_reload_loads_objects_from_file(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()

        obj_key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(obj_key, self.storage._FileStorage__objects)

        reloaded_obj = self.storage._FileStorage__objects[obj_key]
        self.assertEqual(reloaded_obj.__dict__, obj.__dict__)


if __name__ == '__main__':
    unittest.main()
