#!/user/bin/python3
"""Tests for models/review.py"""

import os
import unittest
from datetime import datetime
from models.review import Review
from models.engine.file_storage import FileStorage

# defines variables to use in test
r1 = Review()

# parse kwargs
obj_dict = r1.to_dict()
r2 = Review(**obj_dict)

# parse args
args = ("487", "1245-1528456-158945", "Great place ever!")
r3 = Review(*args)


class TestReview(unittest.TestCase):
    """Defines test cases for Review class"""

    def setUp(self):
        pass  # do nothing

    def tearDown(self):
        """empty __objects and deletes file.json"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_initialization(self):
        """tests for Review class init method"""
        # check if attr in obj
        self.assertIn("id", obj_dict.keys())
        self.assertIn("created_at", obj_dict.keys())
        self.assertIn("updated_at", obj_dict.keys())

        # check if of correct data type
        self.assertIsInstance(r1.id, str)
        self.assertIsInstance(r1.created_at, datetime)
        self.assertIsInstance(r1.updated_at, datetime)

        # check if values are equal
        self.assertEqual(r1.id, r2.id)

    def test_parameters(self):
        """tests the parameters parsed to Review class"""
        # check values
        r1.place_id = "845"
        r1.user_id = "1534-1586-3254-2687"
        self.assertEqual(r3.text, "")  # does not take *args
        self.assertEqual(r1.place_id, "845")

        # check if of correct data type
        self.assertIsInstance(r1.place_id, str)
        self.assertIsInstance(r1.user_id, str)
        self.assertIsInstance(r1.text, str)

    def test_str(self):
        """tests the str method"""
        obj_str = "[{}] ({}) {}".format(
            type(r1).__name__,
            r1.id,
            r1.__dict__
        )
        self.assertEqual(r1.__str__(), obj_str)

    def test_save(self):
        """tests the save method"""
        old_updated_at = r1.updated_at
        r1.save()
        self.assertNotEqual(r1.updated_at, old_updated_at)

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
        self.assertEqual(type(r1).__name__, obj_dict["__class__"])


if __name__ == "__main__":
    unittest.main()
