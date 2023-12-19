#!/usr/bin/python3
"""Defines City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """creates city record"""
    name = ""
    state_id = ""
