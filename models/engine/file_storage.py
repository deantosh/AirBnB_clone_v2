#!/usr/bin/python3
"""Defines a class FileStorage.
   This class:
      - serializes instances to a JSON file
      - deseriallizes JSON file to instances
"""

import os
import json
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage:
    """
    defines file storage class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        returns: __objects dictionary
        """
        if cls:
            cls_dict = {}
            # Loop through all objects
            for k, v in FileStorage.__objects.items():
                if cls == v.__class__ or cls == v.__class__.__name__:
                    cls_dict[k] = v
            return cls_dict

        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key '<obj class name>.id'
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the json file at __file_path
        """
        with open(FileStorage.__file_path, "w") as file:
            json.dump(
                {k: v.to_dict()
                 for k, v in FileStorage.__objects.items()}, file)

    def reload(self):
        """
        deserializes the JSON file to __objects only if the file exists
        """
        class_list = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        if not os.path.exists(FileStorage.__file_path):
            return
        else:
            with open(FileStorage.__file_path, "r") as file:
                obj = None

                # handle error if it fails to deserialize
                try:
                    obj = json.load(file)
                except json.JSONDecodeError:
                    pass

                if obj is None:
                    return

                FileStorage.__objects = {
                    k: class_list[k.split(".")[0]](**v)
                    for k, v in obj.items()
                }

    def delete(self, obj=None):
        """Deletes obj from __objects"""
        if obj:
            # create key used to search the obj
            key = ("{}.{}").format(type(obj).__name__, obj.id)

            # check if key exists
            if key in FileStorage.__objects.keys():
                # delete obj
                del FileStorage.__objects[key]

    def close(self):
        """deserialize the JSON file to objects"""
        self.reload()
