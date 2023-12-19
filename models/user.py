#!/usr/bin/python3
"""
Defines a class User, a child class of BaseModel class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Creates a new User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
