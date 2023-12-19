#!/user/bin/python3
"""Tests for models/place.py"""

import os
import unittest
from datetime import datetime
from models.place import Place
from models.engine.file_storage import FileStorage

# defines variables to use in test
p1 = Place()

# parse kwargs
obj_dict = p1.to_dict()
p2 = Place(**obj_dict)

# parse args
args = ("Mombasa", "001")
p3 = Place(*args)


class TestPlace(unittest.TestCase):
    """Defines test cases for Place class"""

    def setUp(self):
        pass  # do nothing

    def tearDown(self):
        """empty __objects and deletes file.json"""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_initialization(self):
        """tests for Place class init method"""
        # check if attr in obj
        self.assertIn("id", obj_dict.keys())
        self.assertIn("created_at", obj_dict.keys())
        self.assertIn("updated_at", obj_dict.keys())

        # check if of correct data type
        self.assertIsInstance(p1.id, str)
        self.assertIsInstance(p1.created_at, datetime)
        self.assertIsInstance(p1.updated_at, datetime)

        # check if values are equal
        self.assertEqual(p1.id, p2.id)

    def test_parameters(self):
        """tests the parameters parsed to City class"""
        # check values
        p1.name = "Lavington"
        p1.city_id = "047"
        self.assertEqual(p3.name, "")  # does not take args
        self.assertEqual(p1.name, "Lavington")
        self.assertNotEqual(p1.name, p2.name)

        # check if of correct data type
        self.assertIsInstance(p1.city_id, str)
        self.assertIsInstance(p1.user_id, str)
        self.assertIsInstance(p1.name, str)
        self.assertIsInstance(p1.description, str)
        self.assertIsInstance(p1.number_rooms, int)
        self.assertIsInstance(p1.number_bathrooms, int)
        self.assertIsInstance(p1.max_guest, int)
        self.assertIsInstance(p1.price_by_night, int)
        self.assertIsInstance(p1.latitude, float)
        self.assertIsInstance(p1.longitude, float)
        self.assertIsInstance(p1.amenity_ids, list)

    def test_str(self):
        """tests the str method"""
        obj_str = "[{}] ({}) {}".format(
            type(p1).__name__,
            p1.id,
            p1.__dict__
        )
        self.assertEqual(p1.__str__(), obj_str)

    def test_save(self):
        """tests the save method"""
        old_updated_at = p1.updated_at
        p1.save()
        self.assertNotEqual(p1.updated_at, old_updated_at)

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
        self.assertEqual(type(p1).__name__, obj_dict["__class__"])


if __name__ == "__main__":
    unittest.main()
