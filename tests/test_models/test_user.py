#!/usr/bin/python3
"""Defines tests for models/user.py"""

import os
import models
import unittest
from models.user import User
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """tests User model"""

    def setUp(self):
        pass  # do nothing

    def tearDown(self):
        """empty the __objects and deletes the file created"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_initialization(self):
        """test init without parameters"""
        usr1 = User()
        usr2 = User(**usr1.to_dict())
        self.assertIsInstance(usr1.id, str)
        self.assertIsInstance(usr1.created_at, datetime)
        self.assertIsInstance(usr1.updated_at, datetime)
        self.assertIsInstance(usr1.last_name, str)
        self.assertEqual(usr1.updated_at, usr2.updated_at)

    def test_parameters(self):
        """tests User class parameters"""
        usr1 = User()
        self.assertIsInstance(usr1.email, str)
        self.assertIsInstance(usr1.password, str)
        self.assertIsInstance(usr1.first_name, str)
        self.assertIsInstance(usr1.last_name, str)
        key = "{}.{}".format(type(usr1).__name__, usr1.id)
        obj_dict = models.storage.all()
        self.assertIn(key, obj_dict.keys())

    def test_str(self):
        """tests string representation"""
        usr1 = User()
        obj_str = "[{}] ({}) {}".format(
            type(usr1).__name__, usr1.id, usr1.__dict__)
        self.assertEqual(usr1.__str__(), obj_str)

    def test_save(self):
        """tests if updated_at has been updated"""
        usr1 = User()
        old_updated_at = usr1.updated_at
        usr1.save()  # update new time
        self.assertNotEqual(usr1.updated_at, old_updated_at)

    def test_to_dict(self):
        """tests obj dict returned"""
        usr1 = User()
        obj_dict = usr1.to_dict()
        usr2 = User(**obj_dict)
        self.assertIsInstance(obj_dict, dict)
        self.assertIn("created_at", obj_dict.keys())
        self.assertIn("updated_at", obj_dict.keys())
        self.assertEqual(obj_dict["__class__"], type(usr1).__name__)
        self.assertNotEqual(usr1, usr2)


if __name__ == "__main__":
    unittest.main()
