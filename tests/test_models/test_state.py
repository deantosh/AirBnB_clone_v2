#!/usr/bin/python3
"""Tests for models/state.py"""

import os
import unittest
from models import storage
from datetime import datetime
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """defines test cases for State class"""

    def setUp(self):
        pass  # do nothing

    def tearDown(self):
        """empty __objects dict and delete file.json"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_initialization(self):
        """tests for City class init method"""
        s1 = State()
        s2 = State(**s1.to_dict())
        self.assertIsInstance(s1.id, str)
        self.assertIsInstance(s1.created_at, datetime)
        self.assertIsInstance(s1.updated_at, datetime)
        self.assertEqual(s1.updated_at, s2.updated_at)

    def test_parameters(self):
        """test for parameters parsed to City class"""
        state = State()
        key = "{}.{}".format(type(state).__name__, state.id)
        obj_dict = storage.all()
        self.assertIn(key, obj_dict.keys())
        self.assertIsInstance(state.name, str)
        state.name = "Nairobi"
        self.assertEqual(state.name, "Nairobi")

    def test_str(self):
        """tests string rep of the object"""
        state = State()
        obj_str = "[{}] ({}) {}".format(
            type(state).__name__,
            state.id,
            state.__dict__
        )
        self.assertEqual(state.__str__(), obj_str)

    def test_save(self):
        """tests the updated at attribute"""
        state = State()
        old_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(state.updated_at, old_updated_at)

    def test_to_dict(self):
        """tests the obj dict returned"""
        state = State()
        obj_dict = state.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(type(state).__name__, obj_dict["__class__"])
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
