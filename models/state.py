#!/usr/bin/python3
"""Defines a State class"""

from sqlalchemy import Column, String
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """creates the state record -- DB Storage"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', backref='state', cascade="all, delete-orphan")

    # create a state object -- FileStorage
    def __init__(self, name, *args, **kwargs):
        """initialize the state class"""
        super().__init__(args, kwargs)
        self.name = name

    @property
    def cities(self):
        """returns list of City instances with state_id ==
           current state_id.
           This estabishes the FileStorage relationship between
           State and City.
        """
        city_list = []
        for city_obj in models.storage.all(City).values():
            if city_obj.state_id == self.id:
                city_list.append(city_obj)
        return city_list
