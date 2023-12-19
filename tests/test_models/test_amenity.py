#!/usr/bin/python3
"""Tests for models/state.py"""

import os
import unittest
from models import storage
from datetime import datetime
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """defines test cases for Amenity class"""

    def setUp(self):
        pass  # do nothing

    def tearDown(self):
        """empty __objects dict and delete file.json"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_initialization(self):
        """tests for City class init method"""
        a1 = Amenity()
        a2 = Amenity(**a1.to_dict())
        self.assertIsInstance(a1.id, str)
        self.assertIsInstance(a1.created_at, datetime)
        self.assertIsInstance(a1.updated_at, datetime)
        self.assertEqual(a1.updated_at, a2.updated_at)

    def test_parameters(self):
        """test for parameters parsed to City class"""
        a = Amenity()
        key = "{}.{}".format(type(a).__name__, a.id)
        obj_dict = storage.all()
        self.assertIn(key, obj_dict.keys())
        self.assertIsInstance(a.name, str)
        a.name = "Near a supermarket"
        self.assertEqual(a.name, "Near a supermarket")

    def test_str(self):
        """tests string rep of the object"""
        a = Amenity()
        obj_str = "[{}] ({}) {}".format(
            type(a).__name__,
            a.id,
            a.__dict__
        )
        self.assertEqual(a.__str__(), obj_str)

    def test_save(self):
        """tests the updated at attribute"""
        a = Amenity()
        old_updated_at = a.updated_at
        a.save()
        self.assertNotEqual(a.updated_at, old_updated_at)

    def test_to_dict(self):
        """tests the obj dict returned"""
        a = Amenity()
        obj_dict = a.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(type(a).__name__, obj_dict["__class__"])
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
