"""
   Defines tests for file_storage.py in models/engine
   Test classes include:
                test_strorage_initialize
                testFileStorage_methods
"""

import unittest
import os
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_initialize(unittest.TestCase):
    """defines tests for file storage when instantiated"""

    def test_initialize_with_args(self):
        with self.assertRaises(TypeError) as e:
            FileStorage(None)

    def test_initialize_without_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_file_path_is_str(self):
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_objects_is_dict(self):
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_storage_var_is_file_storage(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """defines tests for methods file storage class"""

    def setUp(self):
        pass

    def tearDown(self):
        """empty file storage data and delete file with data if it exists"""
        FileStorage.__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all_no_args(self):
        self.assertEqual(type(models.storage.all()), dict)

    def test_all_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm_obj = BaseModel()
        models.storage.new(bm_obj)
        self.assertIn(
            "BaseModel." + str(bm_obj.id), models.storage.all().keys())

    def test_new_no_args(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        bm_obj = BaseModel()
        models.storage.new(bm_obj)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as file:
            save_text = file.read()
        self.assertIn("BaseModel." + str(bm_obj.id), save_text)

    def tets_save_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm_obj = BaseModel()
        models.storage.new(bm_obj)
        models.storage.save()
        models.storage.reload()
        obj_list = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm_obj.id, obj_list)

    def test_reload_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
