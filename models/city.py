#!/usr/bin/python3
"""Defines City class"""

from sqlalchemy import Column, String, ForeignKey
from models.base_model import Base, BaseModel


class City(BaseModel, Base):
    """creates city record"""
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
