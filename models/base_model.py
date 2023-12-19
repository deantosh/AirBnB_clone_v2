#!/usr/bin/python3
"""
   Defines Base class that defines all common
   attributes/methods for other classes
"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """defines a base class"""

    def __init__(self, *args, **kwargs):
        """intialize base class"""
        if kwargs:
            for key, value in kwargs.items():
                # do not add __class__ to object
                if key == "__class__":
                    continue
                # convert str to datetime
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                # set object attribute
                setattr(self, key, value)
        else:
            # if dict not parsed
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            # link to storage -- set obj to __objects
            models.storage.new(self)

    def __str__(self):
        """returns: str representation of the object"""
        obj_str = "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)
        return obj_str

    def save(self):
        """updates updated_at time with current datetime"""
        self.updated_at = datetime.now()

        # link to storage -- saves __objects to file
        models.storage.save()

    def to_dict(self):
        """returns:obj dict containing all key/values of the instance"""
        # copy obj dict / to alter
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()

        return obj_dict
