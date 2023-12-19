#!/user/bin/python3
"""Tests for City class"""

import os
import unittest
from datetime import datetime
from models.city import City
from models.engine.file_storage import FileStorage

# defines variables to use in test
c1 = City()

# parse kwargs
obj_dict = c1.to_dict()
c2 = City(**obj_dict)

# parse args
args = ("Mombasa", "001")
c3 = City(*args)


class TestCity(unittest.TestCase):
    """Defines test cases for City class"""

    def setUp(self):
        pass  # do nothing

    def tearDown(self):
        """empty __objects and deletes file.json"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_initialization(self):
        """tests for City class init method"""
        # check if attr in obj
        self.assertIn("id", obj_dict.keys())
        self.assertIn("created_at", obj_dict.keys())
        self.assertIn("updated_at", obj_dict.keys())

        # check if of correct data type
        self.assertIsInstance(c1.id, str)
        self.assertIsInstance(c1.created_at, datetime)
        self.assertIsInstance(c1.updated_at, datetime)

        # check if values are equal
        self.assertEqual(c1.id, c2.id)

    def test_parameters(self):
        """tests the parameters parsed to City class"""
        # check values
        c1.name = "Nairobi"
        c1.state_id = "001"
        self.assertEqual(c3.name, "")
        self.assertEqual(c1.name, "Nairobi")
        self.assertNotEqual(c1.name, c2.name)
        # check if of correct data type
        self.assertIsInstance(c1.state_id, str)
        self.assertIsInstance(c1.name, str)

    def test_str(self):
        """tests the str method"""
        obj_str = "[{}] ({}) {}".format(
            type(c1).__name__,
            c1.id,
            c1.__dict__
        )
        self.assertEqual(c1.__str__(), obj_str)

    def test_save(self):
        """tests the save method"""
        old_updated_at = c1.updated_at
        c1.save()
        self.assertNotEqual(c1.updated_at, old_updated_at)

    def test_to_dict(self):
        """tests to_dict method"""
        # test if is of data type
        self.assertIsInstance(obj_dict, dict)

        # test if attr is in dict
        self.assertIn("__class__", obj_dict.keys())
        self.assertIn("created_at", obj_dict.keys())
        self.assertIn("updated_at", obj_dict.keys())

        # test if attr value is of correct type
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)

        # test if correct classname added
        self.assertEqual(type(c1).__name__, obj_dict["__class__"])


if __name__ == "__main__":
    unittest.main()
