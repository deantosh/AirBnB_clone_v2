"""tests for the base_model module"""

import os
import json
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
import time
import uuid


class BaseTest(unittest.TestCase):
    """defines the test cases of the base_model class"""

    def setUp(self):
        pass  # do nothing

    def tearDown(self):
        # empty obj data / delete json file that stores it
        FileStorage.__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_initialization(self):
        """Test method for base model initialization"""
        obj = BaseModel()
        obj_uuid = str(uuid.uuid4())
        k_obj = BaseModel(id=obj_uuid, name="Deantosh Daiddoh", city="Mombasa")
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(str(type(obj)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(k_obj.id, str)
        self.assertEqual(k_obj.id, obj_uuid)
        self.assertEqual(k_obj.name, "Deantosh Daiddoh")
        self.assertEqual(k_obj.city, "Mombasa")

    def test_save(self):
        """Test method for save"""
        obj = BaseModel()
        # delay executing
        time.sleep(0.8)
        date_now = datetime.now()
        obj.save()
        diff = obj.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_dict(self):
        """Test method for dict"""
        obj = BaseModel()
        o_id = str(uuid.uuid4())
        obj1 = BaseModel(id=o_id, name="Kate", country="Nigeria")
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], type(obj).__name__)
        self.assertIn("id", obj_dict.keys())
        self.assertIn("created_at", obj_dict.keys())
        self.assertIn("updated_at", obj_dict.keys())
        with self.assertRaises(KeyError) as e:
            obj1.to_dict()

    def test_str(self):
        """Test method for string representation"""
        obj = BaseModel()
        my_str = "[{}] ({}) {}".format(
            type(obj).__name__, obj.id, obj.__dict__)
        self.assertEqual(obj.__str__(), my_str)


if __name__ == "__main__":
    unittest.main()
