#!/usr/bin/python3
"""Defines City class"""

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class City(BaseModel, Base):
    """creates city record"""
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship(
        'Place', backref='cities', cascade='all, delete-orphan')

    # Create instance for -- FileStorage
    def __init__(self, name, state_id, *args, **kwargs):
        """initialize City class"""
        super().__init__(args, kwargs)
        self.name = name
        self.state_id = state_id
